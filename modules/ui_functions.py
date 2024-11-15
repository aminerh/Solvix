# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from sqlalchemy import  text
from sqlalchemy.exc import SQLAlchemyError

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = 200
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                # if widthLeftBox != 0:
                #     style = self.ui.toggleLeftBox.styleSheet()
                #     self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, width, "right")

    def start_box_animation(self, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # # Check values
        # if left_box_width == 0 and direction == "left":
        #     left_width = 240
        # else:
        #     left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       


        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        # self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # get user full name
    def getuserinfo(self):
        try:
            query = f"""select UTLUTI from AMAZONBD.hlutilp where UTCUTI = '{User.REFUSER}'"""
            self.RefConenctor.ReflexCursor.execute(query)
            result = self.RefConenctor.ReflexCursor.fetchall()
            User.REFFULLNAME=result[0][0].strip()
        except Exception as error:
            print(f"Error while connecting to REFLEX: {error}")
        
    # retreive data from database of anomalies table
    def getAnomalies(self):
        with self.SolvixConenctor.SolviXengine.connect() as connection:
            trans = connection.begin()
            try:
                query = text("""SELECT anomalies.*,"Date Declaration",Case when "POST" is null then 'non trouvé' else "POST" end as "POST avec Surplus" FROM anomalies Left outer join public."Surplus" on "ASIN"="Asin" order by "Date CPT","Heure CPT";""")
                result = connection.execute(query)
                records = result.fetchall()
                columns = result.keys()
                trans.commit()
                # Convert the results to a DataFrame
                df = pd.DataFrame(records, columns=columns)
                return df
            except Exception as e:
                # If any error occurs, rollback the transaction
                trans.rollback()
                print(f"Error during transaction: {e}")
                return None
            
    # refresh anomalies database based on reflex data 
    def refreshDBwithanomalies(self):
        try:
     
            self.RefConenctor.ReflexCursor.execute(Settings.PICK_ANOMALIES)
            result = self.RefConenctor.ReflexCursor.fetchall()

            # Get column headers
            headers = [column[0] for column in self.RefConenctor.ReflexCursor.description]

            # Clean up and convert the data into a DataFrame
            data = [[str(item).strip() if item is not None else "" for item in row] for row in result]
            df = pd.DataFrame(data, columns=headers)
            # SolviXengine = create_engine(f'postgresql://Usolvix:1234@10.49.0.179:5432/Solvix')


            # Start a connection and transaction
            with self.SolvixConenctor.SolviXengine.connect() as connection:
                # Start a transaction
                trans = connection.begin()
                try:
                    # Step 1: Delete existing records from anomalies table
                    delete_query = text("DELETE FROM anomalies;")
                    connection.execute(delete_query)
                    print("Old records deleted from 'anomalies' table.")

                    # Step 2: Insert the new data into the anomalies table
                    df.to_sql('anomalies', self.SolvixConenctor.SolviXengine, if_exists='append', index=False)
                    print("New data inserted successfully into 'anomalies' table.")

                    for index, row in df.iterrows():
                        order_id = row['Commande']  # Assuming order_id is a column in your fetched data

                        # Query to check if order_id exists in the order_log table
                        check_query = text("SELECT COUNT(*) FROM order_actions_log WHERE order_id = :order_id")
                        result = connection.execute(check_query, {'order_id': order_id}).scalar()

                        if result == 0:
                            # Insert new log entry if order_id doesn't exist
                            insert_query = text("""
                                INSERT INTO public.order_actions_log (order_id, action,user_id,old_value,new_value,state) 
                                                VALUES (:order_id, 'INIT','BOT','init state','init state',0)
                            """)
                            connection.execute(insert_query, {'order_id': order_id})
                            print(f"New entry added to 'order_log' for order_id: {order_id}")

                    # Commit the transaction
                    trans.commit()
                except Exception as e:
                    # If any error occurs, rollback the transaction
                    trans.rollback()
                    print(f"Error during transaction: {e}")

        except SQLAlchemyError as e:
            print(f"Error executing SQL: {e}")
        except Exception as e:
            print(f"Error: {e}")

    # refresh surplus database based on reflex data
    def refreshDBSurplus(self):
        try:
     
            self.RefConenctor.ReflexCursor.execute(Settings.SURPLUS)
            result = self.RefConenctor.ReflexCursor.fetchall()

            # Get column headers
            headers = [column[0] for column in self.RefConenctor.ReflexCursor.description]

            # Clean up and convert the data into a DataFrame
            data = [[str(item).strip() if item is not None else "" for item in row] for row in result]
            df = pd.DataFrame(data, columns=headers)
            # SolviXengine = create_engine(f'postgresql://Usolvix:1234@10.49.0.179:5432/Solvix')
            
            df['MISSION'] = df['SPAMIS'].astype(str) +'/'+ df['SPNMIS'].astype(str)
      
            df['Year'] = df['SPSSDC'].astype(str) + df['SPAADC'].astype(str)
            df['SPHHDC'] = df['SPHHDC'].apply(lambda x: x.zfill(6))  # Ensure it has 6 characters
            df['Hour'] = df['SPHHDC'].str[:2].astype(int)    # First two chars are hours
            df['Minute'] = df['SPHHDC'].str[2:4].astype(int) # Next two chars are minutes
            df['Second'] = df['SPHHDC'].str[4:6].astype(int) # Last two chars are seconds
            # Step 5: Create the Datetime by combining Year, Month, Day, Hour, Minute, and Second
            df['Date Declaration'] = pd.to_datetime(df[['Year', 'SPMMDC', 'SPJJDC', 'Hour', 'Minute', 'Second']]
                                .rename(columns={'Year':'year', 'SPMMDC':'month', 'SPJJDC':'day',
                                                 'Hour':'hour', 'Minute':'minute', 'Second':'second'}))
            df =df.rename(columns={'SPNSUP':'SUPPORT','SPCART':'ASIN','SPNBAC':'TSX','SPQTSP':'QUANTITY','SPPOST':'POST','SPDPCK':'ID_PICK','SPNPAC':'ID_PACK','SPCEZM':'Emp_Org'})
            df =df.drop(['SPSSDC','SPAADC','SPMMDC','SPJJDC','SPHHDC','Year','Hour','Minute','Second','SPAMIS','SPNMIS'], axis=1)
  
            # Start a connection and transaction
            with self.SolvixConenctor.SolviXengine.connect() as connection:
                # Start a transaction
                trans = connection.begin()
                try:
                    # Step 1: Delete existing records from anomalies table
                    delete_query = text("""DELETE FROM "Surplus";""")
                    connection.execute(delete_query)
                    print("Old records deleted from 'Surplus' table.")

                    # Step 2: Insert the new data into the anomalies table
                    df.to_sql('Surplus', self.SolvixConenctor.SolviXengine, if_exists='append', index=False)
                    print("New data inserted successfully into 'Surplus' table.")

                    for index, row in df.iterrows():
                        datetime = row['Date Declaration']  # Assuming order_id is a column in your fetched data

                        # Query to check if order_id exists in the order_log table
                        check_query = text("""SELECT COUNT(*) FROM bdd_surplus WHERE "Date Declaration" = '"""+str(datetime)+"'")
                        result = connection.execute(check_query).scalar()

                        if result == 0:
                            # Insert new log entry if order_id doesn't exist
                            insert_query = text("""
                               INSERT INTO public.bdd_surplus(
                                "Date Declaration", "POST", "ASIN", "SUPPORT", "QUANTITY", "TSX", "MISSION", "ID_PICK", "ID_PACK", "Emp_Org")
                                VALUES (:dateime, :post,:asin ,:support,:quantite,:tsx, :mission,:id_pick, :id_pack, :emp_org);
                            """)
                            # Define the parameters
                            params = {
                                'dateime': datetime,  # Example datetime value
                                'post': row['POST'],            # Replace with actual post value
                                'asin': row['ASIN'],                  # Replace with actual ASIN value
                                'support': row['SUPPORT'],          # Replace with actual support type
                                'quantite': row['QUANTITY'],                    # Replace with actual quantity
                                'tsx': row['TSX'],                 # Replace with actual TSX value
                                'mission': row['MISSION'],          # Replace with actual mission type
                                'id_pick': row['ID_PICK'],                    # Replace with actual ID_PICK value
                                'id_pack': row['ID_PACK'],                    # Replace with actual ID_PACK value
                                'emp_org': row['Emp_Org']                # Replace with actual employee organization value
                            }
                            connection.execute(insert_query,params)
                            print(f"New entry added to 'bdd_surplus' for datetime: {datetime}")

                    # Commit the transaction
                    trans.commit()
                except Exception as e:
                    # If any error occurs, rollback the transaction
                    trans.rollback()
                    print(f"Error during transaction: {e}")

        except SQLAlchemyError as e:
            print(f"Error executing SQL: {e}")
        except Exception as e:
            print(f"Error: {e}")

    # retreive data from database of bdd_surplus table
    def getSurplus(self):
        with self.SolvixConenctor.SolviXengine.connect() as connection:
            trans = connection.begin()
            try:
                query = text(""" SELECT "POST","ASIN","SUPPORT","QUANTITY" ,"TSX","MISSION", "ID_PICK" as "PICKEUR" ,"ID_PACK" as "PACKEUR" ,"Emp_Org","Date Declaration" ,state FROM  public.bdd_surplus WHERE (state = 0 or state =1) Order by "Date Declaration" DESC """)
                result = connection.execute(query)
                records = result.fetchall()
                columns = result.keys()
             
                trans.commit()
                # Convert the results to a DataFrame
                df = pd.DataFrame(records, columns=columns)
                return df
            except Exception as e:
                # If any error occurs, rollback the transaction
                trans.rollback()
                print(f"Error during transaction: {e}")
                return None

    #function to add manually a overage
    def addnewSurplus(self,Asin,picking_user,Mission,quantite,Emp_initial,hospital_emp) :
        with self.SolvixConenctor.SolviXengine.connect() as connection:
            # Start a transaction
            trans = connection.begin()
            try:
                insert_query = text("""INSERT INTO public.hospital (asin, solver_id,mission,picker_id,quantité,initial_location,hospital_location)
                        VALUES (:asin,:solver_id,:mission,:picking_user,:quantite,:initial_location,:hospital_emp)""")
                connection.execute(insert_query, {'asin': Asin,'solver_id':User.REFFULLNAME, 'mission':Mission,'picking_user':picking_user,'quantite':quantite,'initial_location':Emp_initial,'hospital_emp':hospital_emp})

     
                trans.commit()



            except Exception as e:
                # If any error occurs, rollback the transaction
                trans.rollback()
                print(f"Error during transaction: {e}")
    
    def restockageSurplus(self,df):
         # Start a connection and transaction
        with self.SolvixConenctor.SolviXengine.connect() as connection:
            # Start a transaction
            trans = connection.begin()
            try:
                for index, row in df.iterrows():
                    datetime = row['Date Declaration']  # Assuming order_id is a column in your fetched data

                    # Query to check if order_id exists in the order_log table
                    check_query = text("""SELECT COUNT(*) FROM bdd_surplus WHERE "Date Declaration" = '"""+str(datetime)+"'")
                    result = connection.execute(check_query).scalar()

                    if result == 1:
                        # Insert new log entry if order_id doesn't exist
                        update_query = text("""
                            UPDATE public.bdd_surplus
                            SET  state=2 ,id_ps_destockage = '"""+User.REFFULLNAME+"""'
                            WHERE "Date Declaration" = '"""+str(datetime)+"'")
                        connection.execute(update_query)
                        print(f"an update been at 'bdd_surplus' for datetime: {datetime}")

                # Commit the transaction
                trans.commit()
            except Exception as e:
                # If any error occurs, rollback the transaction
                trans.rollback()
                print(f"Error during transaction: {e}")
    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
