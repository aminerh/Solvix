import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox,
    QPushButton, QVBoxLayout, QWidget, QHBoxLayout
)
from PySide6.QtCore import Qt
from queries import * 


class MainWindow(QMainWindow):
    def __init__(self,conn):
        super().__init__()

        self.setWindowTitle("Table with Actions")
        self.setGeometry(10, 10, 800, 600)  # Initial geometry; will be full screen later
        self.showFullScreen()  # Make the window full screen
        self.conn = conn  # Keep the database connection

        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.table = QTableWidget(self)
      

        # Set table style
        self.table.setStyleSheet("background-color: lightgray;")  # Set table background color
        self.table.setAlternatingRowColors(True)  # Enable alternating row colors
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: lightgray; /* Gray background */
                gridline-color: black; /* Gridline color */
            }
            QHeaderView::section {
                background-color: darkgray; /* Header background color */
                color: white; /* Header text color */
                padding: 4px; /* Padding for header cells */
                font-weight: bold; /* Bold header text */
            }
            QTableWidget::item {
                padding: 8px; /* Padding for table items */
            }
            QPushButton {
                background-color: blue; /* Button background color */
                color: white; /* Button text color */
                border: none; /* No border */
                border-radius: 4px; /* Rounded corners */
                padding: 5px; /* Padding inside button */
            }
            QPushButton:hover {
                background-color: darkblue; /* Darker button on hover */
            }
        """)

             # Populate the table with data from the anomalies
        self.populate_table()
        # Add table to the layout
        layout.addWidget(self.table)

  
    #     self.table.setCellWidget(row, 2, action_button)

    def on_button_click(self, row):
        """Action to perform when button is clicked."""
        item_name = self.table.item(row, 0).text()
        item_value = self.table.item(row, 1).text()
        print(f"Action triggered for {item_name} with value {item_value}")
    
    def populate_table(self):
        """Populate the table with data from the anomalies table."""
        # Fetch anomalies data
        anomalies_df = getAnomalies()

        if anomalies_df is not None and not anomalies_df.empty:
            # Set the number of rows and columns
            self.table.setRowCount(len(anomalies_df))
            self.table.setColumnCount(len(anomalies_df.columns))
            self.table.setHorizontalHeaderLabels(anomalies_df.columns.tolist())

            # Populate the table with data
            for row in range(len(anomalies_df)):
                for col in range(len(anomalies_df.columns)):
                    item = QTableWidgetItem(str(anomalies_df.iat[row, col]))
                    self.table.setItem(row, col, item)

                # Add an action button for each row
                action_button = QPushButton("Action", self)
                action_button.clicked.connect(lambda checked, r=row: self.on_button_click(r))
                self.table.setCellWidget(row, len(anomalies_df.columns), action_button)

