# from queries import * 

# if __name__ == "__main__":
#     # refreshDBwithanomalies()
#     commande_relance("UcLnPXNvm","init state","wave done","stock dispo commande relancé")

# SQL query for fetching data
import psycopg2
from psycopg2 import sql
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

# from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Solvix"
       
        # APPLY TEXTS
        self.setWindowTitle(title)
       

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)

        # login funtion to btn
        widgets.login_button.clicked.connect(self.login)

        #refresh function to btn
        widgets.refresh.clicked.connect(self.RefreshPickAnomalies)

        #logout function to btn
        widgets.btn_logout.clicked.connect(self.logout)



        #  to delete
        # # EXTRA LEFT BOX
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\Solvix_light.qss"

        # SET THEME AND HACKS
        # to check this it s used for what   
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.login)
        widgets.btn_login.setStyleSheet(UIFunctions.selectMenu(widgets.btn_login.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_login":
            # print("Save BTN clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.login) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

      

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')



    def login(self):
        btn = self.sender()
        btnName = btn.objectName()

        username = widgets.username.text()
        password = widgets.password.text()
        Settings.REFUSER=username
        Settings.REFPWD=password
        if len(username) != 8:
            QMessageBox.warning(self, "Erreur", "R520 ou mot de passe incorrecte: " + str(e))
            return 

        if btnName == "login_button":
            print("connection btn clicked")
 
            try:
                conn = pyodbc.connect(
                    'DRIVER={iSeries Access ODBC Driver};'
                    f'SYSTEM=TDCRFX52;'
                    f'UID={username};'
                    f'PWD={password};'
                )
                QMessageBox.information(self, "Succès", "Connexion réussie !")
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                self.GetPickAnomalies()
            except pyodbc.Error as e:
                QMessageBox.warning(self, "Erreur", "Connexion échouée: " + str(e))

    def GetPickAnomalies(self):
       
        anomalies_df = UIFunctions.getAnomalies(self)

        if anomalies_df is not None and not anomalies_df.empty:
            # Set the number of rows and columns
            widgets.PickAnomalies.setRowCount(len(anomalies_df))
            widgets.PickAnomalies.setColumnCount(len(anomalies_df.columns))
            widgets.PickAnomalies.setHorizontalHeaderLabels(anomalies_df.columns.tolist())

            # Populate the table with data
            for row in range(len(anomalies_df)):
                for col in range(len(anomalies_df.columns)):
                    item = QTableWidgetItem(str(anomalies_df.iat[row, col]))
                    widgets.PickAnomalies.setItem(row, col, item)
                
    def RefreshPickAnomalies(self):
        btn = self.sender()
        btnName = btn.objectName()
        username = widgets.username.text()
        password = widgets.password.text()
        if len(username) > 1 and len(password) > 1:
            if btnName == "refresh":
                # // here
                # # Fetch anomalies data
                anomalies_df = UIFunctions.refreshDBwithanomalies(self)
                self.GetPickAnomalies()
    
    def logout(self):
        btn = self.sender()
        btnName = btn.objectName()
     
        if btnName == "btn_logout":
            widgets.username.setText("")
            widgets.password.setText("")
            Settings.REFUSER=''
            Settings.REFPWD=''
            widgets.PickAnomalies.clear()
            widgets.stackedWidget.setCurrentWidget(widgets.login)


               
        
  

           



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
