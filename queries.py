# queries.py

# SQL query for fetching data
from datetime import datetime
import psycopg2
from psycopg2 import sql
import pandas as pd
import pyodbc

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

current_date = datetime.now().strftime('%Y-%m-%d')
user = "R520MRHA"
pwd = "RH644707!"
#  ' loc AS "Emplacement avec quantité",
#  ' qty AS "Quantité sans prélèvement" ,
#   npcmnp AS "Reason Code",
PICK_ANOMALIES = """
SELECT 
  oerodp AS "Commande",
  OECCPL AS "Type de commande",
  CPT AS "Date CPT",
  CPTTIM AS "Heure CPT",
  DIGITS(pvjvpr) CONCAT '/' CONCAT DIGITS(pvmvpr) CONCAT '/' CONCAT DIGITS(pvsvpr) CONCAT DIGITS(pvavpr) AS "Date du manquant",
  SUBSTR(DIGITS(pvhvpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pvhvpr), 3, 2) AS "Heure du manquant",
  pvcart AS "Asin",
  arlart AS "Description",
  pvqapb AS "Quantité manquante",
  pvc1em CONCAT ' ' CONCAT pvc2em CONCAT ' ' CONCAT pvc3em CONCAT ' ' CONCAT pvc4em CONCAT ' ' CONCAT pvc5em AS "Adresse",
  pvnsup AS "Support",


  case   when loc >= 1 then 'oui' else 'non' end as "a relancé" 
FROM 
  INFSQL.NDDATEP 
  INNER JOIN AMAZONBD.HLPRELP ON pvtvpr = '1' 
    AND pvtnpr = '1' 
    AND pvcdpo = '001' 
    AND pvcact = '001' 
    AND pvsvpr = dasie 
    AND pvavpr = daann 
    AND pvmvpr = damois 
    AND pvjvpr = dajour 
  INNER JOIN AMAZONBD.HLNONPP ON npcact = pvcact 
    AND npcdpo = pvcdpo 
    AND npnann = pvnann 
    AND npnprl = pvnprl
  INNER JOIN AMAZONBD.HLARTIP ON pvcact = arcact 
    AND pvcart = arcart
  LEFT OUTER JOIN AMAZONBD.HLUTILP ON pvcuvp = utcuti
  INNER JOIN 
    (SELECT pecdpo, pecact, penann, penpre, oerodp, peccpl, pecrgc, OECCPL, ORSTAT, ORWAVD, ORWAVT, ORLAUC, ORLAUE, 
      DIGITS(pejdpr) CONCAT '/' CONCAT DIGITS(pemdpr) CONCAT '/' CONCAT DIGITS(pesdpr) CONCAT DIGITS(peadpr) AS CPT, 
      SUBSTR(DIGITS(pehdpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pehdpr), 3, 2) AS CPTTIM 
    FROM AMAZONBD.HLPRENP
    LEFT OUTER JOIN AMAZONBD.HLPRPLP ON pecdpo = p1cdpo 
      AND pecact = p1cact 
      AND penann = p1nanp 
      AND penpre = p1npre
    LEFT OUTER JOIN AMAZONBD.HLODPEP ON pecdod = oecdpo 
      AND p1cact = oecact 
      AND p1nano = oenann 
      AND p1nodp = oenodp
    INNER JOIN AMRFXDD.AIORDEP ON oecdpo = ORCDPO 
      AND oecact = ORCACT 
      AND OERODP = ORRODP
      AND ORSLRR <> 'SUCCESS' 
      AND ORSTAT <>'Floor Denial' 
      AND ORSTAT <>'Cancelled'
    WHERE p1cdpo = '001' 
      AND pecact = '001'
    GROUP BY pecdpo, pecact, penann, penpre, oerodp, peccpl, pecrgc, ORSTAT, OECCPL, ORWAVD, ORWAVT, ORLAUC, ORLAUE, 
      DIGITS(pejdpr) CONCAT '/' CONCAT DIGITS(pemdpr) CONCAT '/' CONCAT DIGITS(pesdpr) CONCAT DIGITS(peadpr), 
      SUBSTR(DIGITS(pehdpr), 1, 2) CONCAT ':' CONCAT SUBSTR(DIGITS(pehdpr), 3, 2)) S
  ON pecdpo = pvcdpo 
    AND pecact = pvcact 
    AND penpre = pvnpre 
    AND penann = pvnanp
  LEFT OUTER JOIN 
    (SELECT gecdpo, gecact, gecart, COUNT(DISTINCT sunemp) AS loc, SUM(geqgei) AS qty
    FROM AMAZONBD.HLGEINP
    INNER JOIN AMAZONBD.HLSUPPP ON sucdpo = gecdpo 
      AND sunsup = gensup
    EXCEPTION JOIN AMAZONBD.HLPRELP ON pvcdpo = gecdpo 
      AND pvcact = gecact 
      AND pvngei = gengei 
      AND pvtvpr = '0'
    EXCEPTION JOIN AMAZONBD.HLLPRGP ON gecdpo = lgcdpo 
      AND gecact = lgcact 
      AND lgngei = gengei
    WHERE gecdpo = '001' 
      AND gecact = '001' 
      AND gecqal = 'STD' 
      AND getgdi = '1'
    GROUP BY gecdpo, gecact, gecart) GG
  ON gecdpo = pvcdpo 
    AND gecact = pvcact 
    AND gecart = pvcart
WHERE  
  DADATE >= '"""+current_date+"""'
  AND NPCMNP <> 'OC'
  AND PVC1EM NOT LIKE 'BA%%' 
  AND PVC1EM NOT LIKE 'BB%%' 
  AND PVC1EM NOT LIKE 'BC%%' 
  AND PVC1EM NOT LIKE 'BD%%' 
  AND PVC1EM NOT LIKE 'BE%%' 
  AND PVC1EM NOT LIKE 'BF%%' 
  AND PVC1EM NOT LIKE 'BG%%' 
  AND PVC1EM NOT LIKE 'BH%%' 
  AND PVC1EM NOT LIKE 'BK05' 
  AND PVC1EM NOT LIKE 'BK04' 
  AND PVC1EM NOT LIKE 'VS%%' 
  AND PVC1EM NOT LIKE 'DA%%' 
  AND PVC1EM NOT LIKE 'DB%%' 
  AND PVC1EM NOT LIKE 'DC%%' 
  AND PVC1EM NOT LIKE 'FURN%%' 
  AND oerodp LIKE 'U%%'
ORDER BY CPT,CPTTIM

"""
try:
    # Connect to PostgreSQL server
    global SolviXconn
    SolviXconn = psycopg2.connect(
        dbname="Solvix",
        user="Usolvix",
        password="1234",
        host="10.49.0.179",  # or the IP address of your server
        port="5432",       # Default PostgreSQL port
    )
    # Create a cursor object
    global SolviXcursor
    SolviXcursor = SolviXconn.cursor()
     
    SolviXengine = create_engine(f'postgresql://Usolvix:1234@10.49.0.179:5432/Solvix')
 
except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

try:
    global ReflexConn
    ReflexConn = pyodbc.connect(
        'DRIVER={iSeries Access ODBC Driver};'
        'SYSTEM=TDCRFX52;'
        'UID=R520MRHA;' # to replace with inputs 
        'PWD=RH644707!'  # Remplace par ton mot de passe
    )
    global ReflexCursor
    ReflexCursor = ReflexConn.cursor()
  
except Exception as e:
    print("error while connection to reflex {e}")

def getAnomalies():
    with SolviXengine.connect() as connection:
        trans = connection.begin()
        try:
            query = text("SELECT * FROM anomalies;")
            result = connection.execute(query)
            records = result.fetchall()
            # Get column names
            columns = result.keys()

            # Commit the transaction (not strictly necessary for SELECT queries)
            trans.commit()

            # Convert the results to a DataFrame
            df = pd.DataFrame(records, columns=columns)

            return df
        except Exception as e:
            # If any error occurs, rollback the transaction
            trans.rollback()
            print(f"Error during transaction: {e}")
            return None

def refreshDBwithanomalies():
    try:
        # Fetch data from ReflexCursor
        ReflexCursor.execute(PICK_ANOMALIES)
        result = ReflexCursor.fetchall()

        # Get column headers
        headers = [column[0] for column in ReflexCursor.description]

        # Clean up and convert the data into a DataFrame
        data = [[str(item).strip() if item is not None else "" for item in row] for row in result]
        df = pd.DataFrame(data, columns=headers)

        # Start a connection and transaction
        with SolviXengine.connect() as connection:
            # Start a transaction
            trans = connection.begin()
            try:
                # Step 1: Delete existing records from anomalies table
                delete_query = text("DELETE FROM anomalies;")
                connection.execute(delete_query)
                print("Old records deleted from 'anomalies' table.")

                # Step 2: Insert the new data into the anomalies table
                df.to_sql('anomalies', SolviXengine, if_exists='append', index=False)
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



def commande_relance(order,old_state,new_state,commentaire) :
    # Start a connection and transaction
  try: 
    with SolviXengine.connect() as connection:
        # Start a transaction
        trans = connection.begin()
        try:
            insert_query = text("""
                INSERT INTO public.order_actions_log (order_id, action, user_id, old_value, new_value, state, remarks) 
                VALUES (:order_id, 'Waved', :user, 'init state', :new_state, 1, :remarks)
            """)

            # Correct the parameter dictionary (no colons in the keys)
            connection.execute(insert_query, {
                'order_id': order,
                'user': user,
                'new_state': new_state,
                'remarks': commentaire
            })
            print(f"Wave done for order_id: {order}")

            # Commit the transaction
            trans.commit()
        except Exception as e:
            # If any error occurs, rollback the transaction
            trans.rollback()
            print(f"Error during transaction: {e}")

  except SQLAlchemyError as e:
    print(f"Error executing SQL: {e}")
