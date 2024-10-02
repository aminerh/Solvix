import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from functools import partial
from queries import *  # Import the query
from datetime import datetime
from MainWindow import MainWindow

# Login window class
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion")
        
        # Set the window to full screen
        self.showFullScreen()

        # Main layout to center the login form
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Top layout for close button
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignRight)

        # Close Button
        self.close_button = QPushButton("X")
        self.close_button.setFixedSize(40, 40)  # Set fixed size for the button
        self.close_button.clicked.connect(self.close_window)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                border-radius: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        # Add the close button to the top layout
        top_layout.addWidget(self.close_button)

        # Logo (place it above the username/password fields)
        form_layout = QVBoxLayout()
        self.logo_label = QLabel()
        pixmap = QPixmap("logo.png")  # Replace with the actual path to your logo image
        pixmap = pixmap.scaled(180, 180, Qt.KeepAspectRatio)  # Resize the logo to fit in the form
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)

        # Username and Password Fields
        self.username_label = QLabel("Utilisateur :")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Mot de passe :")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login Button
        self.login_button = QPushButton("Se connecter")
        self.login_button.clicked.connect(self.check_login)

        # Adding widgets to the form layout
        form_layout.addWidget(self.logo_label)  # Add the logo to the form layout
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)

        # Create a widget to hold the form layout and add it to the center
        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setFixedSize(300, 350)  # Adjust the size to fit the logo and fields

        # Add the form to the main layout (centered)
        main_layout.addLayout(top_layout)  # Add the top layout (close button) first
        main_layout.addWidget(form_widget)

        self.setLayout(main_layout)

        # Set styles
        self.setStyleSheet("""
            QWidget {
                background-color: #D3D3D3;  /* Gray background */
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLabel {
                color: #333;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                margin-top: 15px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    def close_window(self):
        self.close()

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            conn = pyodbc.connect(
                'DRIVER={iSeries Access ODBC Driver};'
                f'SYSTEM=TDCRFX52;'
                f'UID={username};'
                f'PWD={password};'
            )
            QMessageBox.information(self, "Succès", "Connexion réussie !")
            self.main_window = MainWindow(conn)
            self.main_window.show()
            self.close()
        except pyodbc.Error as e:
            QMessageBox.warning(self, "Erreur", "Connexion échouée: " + str(e))


# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
