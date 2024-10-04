
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
        # setting the reflex connection object 
        self.RefConenctor = ReflexConenctor()
        self.SolvixConenctor=SolvixDBConnector()

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
        widgets.btn_surplus.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)

        # login funtion to btn
        widgets.login_button.clicked.connect(self.login)

        #refresh function to btn
        widgets.refresh.clicked.connect(self.RefreshPickAnomalies)

        #logout function to btn
        widgets.btn_logout.clicked.connect(self.logout)

        # add new surplus 
        widgets.new_surplus.clicked.connect(self.new_surplus)



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
        # useCustomTheme = False
        # themeFile = "themes\Solvix_light.qss"

        # # SET THEME AND HACKS
        # # to check this it s used for what   
        # if useCustomTheme:
        #     # LOAD AND APPLY STYLE
        #     UIFunctions.theme(self, themeFile, True)

        #     # SET HACKS
        #     AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.login)
        widgets.btn_login.setStyleSheet(UIFunctions.selectMenu(widgets.btn_login.styleSheet()))
        widgets.btn_home.setVisible(False)
        widgets.btn_surplus.setVisible(False)
        widgets.btn_widgets.setVisible(False)
        widgets.pushButton_2.setVisible(False)
        # widgets.btn_home.setEnabled(False)



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
        

         # SHOW NEW PAGE
        if btnName == "btn_surplus":
            # print("Save BTN clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.surplus) # SET PAGE
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
        User.REFUSER=username
        User.REFPWD=password
        if len(username) != 8:
            toast = Toast(self)
            toast.setDuration(5000)  # Hide after 5 seconds
            toast.setTitle('Erreur ! R520 ou mot de passe incorrecte ')
            toast.applyPreset(ToastPreset.ERROR)  # Apply style preset
            toast.setBackgroundColor(QColor('#282C34'))
            toast.setTitleColor(QColor('#FFFFFF'))
            toast.setDurationBarColor(QColor('#F39E4E'))
            toast.setIconColor(QColor('#F39E4E'))
            toast.setIconSeparatorColor(QColor('#F39E4E'))
            toast.setCloseButtonIconColor(QColor('#F39E4E'))
            toast.show()            
            return 

        if btnName == "login_button":
            print("connection btn clicked")
            
            if self.RefConenctor.connect() : 
                self.GetPickAnomalies()
                UIFunctions.getuserinfo(self)
                widgets.UserInfo.setText(User.REFFULLNAME)
                widgets.btn_home.setVisible(True)
                widgets.btn_surplus.setVisible(True)
                widgets.btn_widgets.setVisible(True)
                widgets.pushButton_2.setVisible(True)
                widgets.btn_login.setVisible(False)
                widgets.stackedWidget.setCurrentWidget(widgets.home) # SET PAGE
                widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
                toast = Toast(self)
                toast.setDuration(5000)  # Hide after 5 seconds
                toast.setTitle('Succès ! Bienvenue '+ User.REFFULLNAME)
                toast.applyPreset(ToastPreset.SUCCESS)  # Apply style preset
                toast.setBackgroundColor(QColor('#282C34'))
                toast.setTitleColor(QColor('#FFFFFF'))
                toast.setDurationBarColor(QColor('#F39E4E'))
                toast.setIconColor(QColor('#F39E4E'))
                toast.setIconSeparatorColor(QColor('#F39E4E'))
                toast.setCloseButtonIconColor(QColor('#F39E4E'))
                toast.show()
            else : 
                toast = Toast(self)
                toast.setDuration(5000)  # Hide after 5 seconds
                toast.setTitle('Erreur ! R520 ou mot de passe incorrecte ')
                toast.applyPreset(ToastPreset.ERROR)  # Apply style preset
                toast.setBackgroundColor(QColor('#282C34'))
                toast.setTitleColor(QColor('#FFFFFF'))
                toast.setDurationBarColor(QColor('#F39E4E'))
                toast.setIconColor(QColor('#F39E4E'))
                toast.setIconSeparatorColor(QColor('#F39E4E'))
                toast.setCloseButtonIconColor(QColor('#F39E4E'))
                toast.show()

            
            

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
            User.REFUSER=''
            User.REFPWD=''
            User.REFFULLNAME=''
            widgets.PickAnomalies.clear()
            widgets.stackedWidget.setCurrentWidget(widgets.login)
            widgets.btn_home.setVisible(False)
            widgets.btn_surplus.setVisible(False)
            widgets.btn_widgets.setVisible(False)
            widgets.pushButton_2.setVisible(False)
            widgets.btn_login.setVisible(True)
            widgets.btn_login.setStyleSheet(UIFunctions.selectMenu(widgets.btn_login.styleSheet()))
    
    def new_surplus(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "new_surplus":
            # Fetch input values
            asin = widgets.Asin.text().strip()
            picking_user = widgets.picking_user.text().strip()
            mission = widgets.Mission.text().strip()
            quantite = widgets.quantite.text().strip()
            emp_initial = widgets.Emp_initial.text().strip()
            hospital_emp = widgets.hospital_emp.currentText().strip()
            print(hospital_emp)
            # Input validation
            if not asin:
                QMessageBox.warning(self, "Input Error", "ASIN cannot be empty.")
                return
            if not picking_user:
                QMessageBox.warning(self, "Input Error", "Picking User cannot be empty.")
                return
            if not mission:
                QMessageBox.warning(self, "Input Error", "Mission cannot be empty.")
                return
            if not quantite or not quantite.isdigit():
                QMessageBox.warning(self, "Input Error", "Quantity must be a valid number.")
                return
            if not emp_initial:
                QMessageBox.warning(self, "Input Error", "Initial Emp cannot be empty.")
                return
            if not hospital_emp:
                QMessageBox.warning(self, "Input Error", "Hospital Emp cannot be empty.")
                return

            # If all validations pass, call the function to add a new surplus
            
            UIFunctions.addnewSurplus(self,asin, picking_user, mission, quantite, emp_initial, hospital_emp)
            toast = Toast(self)
            toast.setDuration(2000)  # Hide after 5 seconds
            toast.setTitle('Succès ! Le nouveau surplus a été ajouté avec succès.')
            toast.applyPreset(ToastPreset.SUCCESS)  # Apply style preset
            toast.show()
            widgets.Asin.setText("")
            widgets.picking_user.setText("")
            widgets.Mission.setText("")
            widgets.quantite.setText("")
            widgets.Emp_initial.setText("")
            widgets.hospital_emp.setCurrentIndex(0)

                
        
  

           



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
