import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QGraphicsScene
from PySide6.QtGui import QPixmap
from ui_login import Ui_MainWindow  # Import the generated UI class
from MainWindow import MainWindow   # Import your MainWindow class

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        
        # Setup the UI (this will initialize all the widgets)
        self.ui.setupUi(self)

        # Set window title and other properties (if needed)
        self.setWindowTitle("Connexion")

       

          # Optionally, add a logo to the QGraphicsView using QGraphicsScene
        pixmap = QPixmap("logo.png")  # Replace with the path to your logo
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.logo.setScene(scene)  # Set the scene in QGraphicsView
        # self.ui.logo.fitInView(scene.itemsBoundingRect())  # Keep aspect ratio


        # Connect buttons to their respective slots
        self.ui.login_button.clicked.connect(self.check_login)

    def check_login(self):
        # Get username and password
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        try:
            # Attempt to connect to the database
            conn = pyodbc.connect(
                'DRIVER={iSeries Access ODBC Driver};'
                f'SYSTEM=TDCRFX52;'
                f'UID={username};'
                f'PWD={password};'
            )
            # If connection is successful, show a success message
            QMessageBox.information(self, "Succès", "Connexion réussie !")

            # Create and show the MainWindow
            self.main_window = MainWindow(conn)
            self.main_window.show()

            # Close the login window
            self.close()
        except pyodbc.Error as e:
            # Show error message if connection fails
            QMessageBox.warning(self, "Erreur", "Connexion échouée: " + str(e))

# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
