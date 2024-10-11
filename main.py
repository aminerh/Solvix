
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
        widgets.btn_pack_station.clicked.connect(self.buttonClick)

        # login funtion to btn
        widgets.login_button.clicked.connect(self.login)
        

        #refresh function to btn
        widgets.refresh.clicked.connect(self.RefreshPickAnomalies)

        #logout function to btn
        widgets.btn_logout.clicked.connect(self.logout)

        # add new surplus 
        widgets.new_surplus.clicked.connect(self.new_surplus)

        # refresh surplus      
        widgets.refresh_stations.clicked.connect(self.refreshPackingStation)

        # search in  surplus      
        widgets.search_by_poste.clicked.connect(self.researchinBDD_surplus)
        

        #add function to print button   
        widgets.btn_print.clicked.connect(self.printCurrentData)
                
        # select all in packing surplus        
        widgets.btn_selectall.clicked.connect(self.buttonClick)
        
        # select all in packing surplus        
        widgets.btn_deselectall.clicked.connect(self.buttonClick)

         # select all in packing surplus        
        widgets.btn_restocker_surplus.clicked.connect(self.buttonClick)
     

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.login)
        widgets.btn_login.setStyleSheet(UIFunctions.selectMenu(widgets.btn_login.styleSheet()))
        widgets.btn_home.setVisible(False)
        widgets.btn_surplus.setVisible(False)
        widgets.btn_widgets.setVisible(False)
        widgets.btn_pack_station.setVisible(False)
    

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

          # SHOW NEW PAGE
        if btnName == "btn_pack_station":
            # print("Save BTN clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.packing_stations) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # select all in surplus declared in stations
        if btnName == "btn_selectall":
            # print("Save BTN clicked!")
            self.select_all()
        
        # deselect all in surplus declared in stations
        if btnName == "btn_deselectall":
            # print("Save BTN clicked!")
            self.deselect_all()
        
        # btn restocker surplus
        if btnName == "btn_restocker_surplus":
            # print("Save BTN clicked!")
            self.restocker()
   

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
                self.GetBDD_Surplus()
                widgets.UserInfo.setText(User.REFFULLNAME)
                widgets.btn_home.setVisible(True)
                widgets.btn_surplus.setVisible(True)
                widgets.btn_widgets.setVisible(True)
                widgets.btn_pack_station.setVisible(True)
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

            for row in range(len(anomalies_df)):
                for col in range(len(anomalies_df.columns)):
                    item = QTableWidgetItem(str(anomalies_df.iat[row, col]))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
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
            widgets.btn_pack_station.setVisible(False)
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
    
    def refreshPackingStation(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "refresh_stations":
            anomalies_df = UIFunctions.refreshDBSurplus(self)
    
    def researchinBDD_surplus(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "search_by_poste":
            searchkey = widgets.poste_search.text()
            self.GetBDD_Surplus(searchkey)
    
    # def GetBDD_Surplus(self, filtre=''):

    #     widgets.packing_status.clearContents()
    #     widgets.packing_status.setRowCount(0)
    #     red_brush = QBrush(QColor(255, 0, 0)) 

    #     surplus_df = UIFunctions.getSurplus(self)

    #     if surplus_df is not None and not surplus_df.empty:
    #         # Apply filter only if the 'filtre' parameter is not empty
    #         if filtre.strip():  # .strip() removes any leading/trailing whitespace
    #             surplus_df = surplus_df[
    #                 (surplus_df['POST'].str.contains(filtre, case=False, na=False)) |
    #                 (surplus_df['ASIN'].str.contains(filtre, case=False, na=False))
    #             ]

    #         if not surplus_df.empty:

    #             widgets.packing_status.setRowCount(len(surplus_df))
    #             widgets.packing_status.setColumnCount(len(surplus_df.columns)) 
               
    #             headers = [col for col in surplus_df.columns if col != 'state']  # Exclude 'state' from headers
    #             headers.append('Select')  #
    
    #             widgets.packing_status.setHorizontalHeaderLabels(headers)

    #             for row in range(len(surplus_df)):
    #                 checkbox_widget = QWidget()
    #                 checkbox_layout = QHBoxLayout()
    #                 checkbox_layout.setAlignment(Qt.AlignCenter)
    #                 checkbox = QCheckBox()
    #                 checkbox_layout.addWidget(checkbox)
    #                 checkbox_widget.setLayout(checkbox_layout)
                    
    #                 for col in range(len(headers)-1):
    #                     item = QTableWidgetItem(str(surplus_df.iat[row, col]))
    #                     print(str(surplus_df.iat[row, col]))
    #                     item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    #                     widgets.packing_status.setItem(row, col , item)  


    #                 # print(surplus_df.columns)
    #                 # if int(surplus_df.iat[row, len(surplus_df.columns)-1]) == 1 :
    #                 #     for c in range(len(headers)-1):
    #                 #        widgets.packing_status.item(row, c).setBackground(red_brush)


    #                 # widgets.packing_status.setCellWidget(row, len(headers), checkbox_widget)             
                     
    #             else:
    #                 widgets.packing_status.clearContents()
    #                 widgets.packing_status.setRowCount(0)
                
    def GetBDD_Surplus(self, filtre=''):

        widgets.packing_status.clearContents()
        widgets.packing_status.setRowCount(0)
        red_brush = QBrush(QColor(255, 0, 0)) 

        df=UIFunctions.getSurplus(self)
        surplus_df = UIFunctions.getSurplus(self).drop(columns=['state'])
        
        if surplus_df is not None and not surplus_df.empty:
            # Apply filter only if the 'filtre' parameter is not empty
            if filtre.strip():  # .strip() removes any leading/trailing whitespace
                surplus_df = surplus_df[
                    (surplus_df['POST'].str.contains(filtre, case=False, na=False)) |
                    (surplus_df['ASIN'].str.contains(filtre, case=False, na=False))
                ]

            if not surplus_df.empty:

                widgets.packing_status.setRowCount(len(surplus_df))
                widgets.packing_status.setColumnCount(len(surplus_df.columns) + 1) 
                headers = surplus_df.columns.tolist() +  ['Select'] 
                widgets.packing_status.setHorizontalHeaderLabels(headers)

                for row in range(len(surplus_df)):
                    checkbox_widget = QWidget()
                    checkbox_layout = QHBoxLayout()
                    checkbox_layout.setAlignment(Qt.AlignCenter)
                    checkbox = QCheckBox()
                    checkbox_layout.addWidget(checkbox)
                    checkbox_widget.setLayout(checkbox_layout)
                    
                    for col in range(len(surplus_df.columns)):
                        item = QTableWidgetItem(str(surplus_df.iat[row, col]))
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                        widgets.packing_status.setItem(row, col , item)  # Data starts from 2nd column (col + 1)
                        
                    if int(surplus_df.iat[row, len(surplus_df.columns)-1]) == 1 :
                        for c in range(len(headers)-2):
                           widgets.packing_status.item(row, c).setBackground(red_brush)
                    widgets.packing_status.setCellWidget(row, len(surplus_df.columns), checkbox_widget)  
            else:
                widgets.packing_status.clearContents()
                widgets.packing_status.setRowCount(0)           

    
    # function to select and deselect item for surplus 

    def select_all(self):
        row_count = widgets.packing_status.rowCount()
        
        for row in range(row_count):
            checkbox_widget = widgets.packing_status.cellWidget(row, widgets.packing_status.columnCount() - 1)
            
            if checkbox_widget is not None:
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox is not None:
                    checkbox.setChecked(True)
    def deselect_all(self):
  
        row_count = widgets.packing_status.rowCount()
        
        for row in range(row_count):
            checkbox_widget = widgets.packing_status.cellWidget(row, widgets.packing_status.columnCount() - 1)
            
            if checkbox_widget is not None:
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox is not None:
                    checkbox.setChecked(False)
    # function to reput in stock all surplus item
    def restocker(self):
        # add qmessagebox to confirm

     
        selected_rows = []
     
        row_count = widgets.packing_status.rowCount()
        col_count = widgets.packing_status.columnCount() - 1  # Exclude the checkbox column
        

        headers = [widgets.packing_status.horizontalHeaderItem(col).text() for col in range(col_count)]
      
        for row in range(row_count):
            
            checkbox_widget = widgets.packing_status.cellWidget(row, col_count)
            
            if checkbox_widget is not None:
         
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox is not None and checkbox.isChecked():
                   
                    row_data = []
                    for col in range(col_count):
                      
                        item = widgets.packing_status.item(row, col)
                        row_data.append(item.text())

                    selected_rows.append(row_data)
        
   
        if selected_rows:
            selected_df = pd.DataFrame(selected_rows, columns=headers)
        else:
            selected_df = pd.DataFrame(columns=headers)
        UIFunctions.restockageSurplus(self,selected_df)
        self.GetBDD_Surplus()
        # function to make status of this order at 2




    def get_table_data(self, table_widget):
        """Retrieves data from a QTableWidget and returns it as a DataFrame."""
        row_count = table_widget.rowCount()
        col_count = table_widget.columnCount()

        data = {}
        for col in range(col_count):
            header = table_widget.horizontalHeaderItem(col).text()
            data[header] = []
            for row in range(row_count):
                item = table_widget.item(row, col)
                data[header].append(item.text() if item else '')

        return pd.DataFrame(data)
    
    def printCurrentData(self):
        current_index = widgets.stackedWidget.currentIndex()
        print(current_index)
        if current_index == 1:
            print("Anomalies Data:")
            df =self.get_table_data(widgets.PickAnomalies)
            df.to_excel("anomalies.xlsx", index=False)
            toast = Toast(self)
            toast.setDuration(5000)  # Hide after 5 seconds
            toast.setTitle('Fichier anomalies.xlsx a été télécharger')
            toast.setPosition(ToastPosition.TOP_RIGHT)  # Default: ToastPosition.BOTTOM_RIGHT
            toast.applyPreset(ToastPreset.SUCCESS)  # Apply style preset
            toast.setBackgroundColor(QColor('#282C34'))
            toast.setTitleColor(QColor('#FFFFFF'))
            toast.setDurationBarColor(QColor('#F39E4E'))
            toast.setIconColor(QColor('#F39E4E'))
            toast.setIconSeparatorColor(QColor('#F39E4E'))
            toast.setCloseButtonIconColor(QColor('#F39E4E'))
            toast.show()


        elif current_index == 3:
            print("Surplus Data:")
            df =self.get_table_data(widgets.packing_status)
            df.to_excel("surplus.xlsx", index=False)
            toast = Toast(self)
            toast.setDuration(5000)  # Hide after 5 seconds
            toast.setTitle('Fichier surplus.xlsx a été télécharger')
            toast.setPosition(ToastPosition.TOP_RIGHT)  # Default: ToastPosition.BOTTOM_RIGHT
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
            toast.setTitle('Aucune donnée disponible pour le téléchargement')
            toast.setPosition(ToastPosition.TOP_RIGHT)  # Default: ToastPosition.BOTTOM_RIGHT
            toast.applyPreset(ToastPreset.ERROR)  # Apply style preset
            toast.setBackgroundColor(QColor('#282C34'))
            toast.setTitleColor(QColor('#FFFFFF'))
            toast.setDurationBarColor(QColor('#F39E4E'))
            toast.setIconColor(QColor('#F39E4E'))
            toast.setIconSeparatorColor(QColor('#F39E4E'))
            toast.setCloseButtonIconColor(QColor('#F39E4E'))
            toast.show()



                
        
  

           



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
