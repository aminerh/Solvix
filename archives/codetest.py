import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

from queries import *  # Import the query
from v1.archives.bdcon import * 


try:
    conn = pyodbc.connect(
        'DRIVER={iSeries Access ODBC Driver};'
        f'SYSTEM=TDCRFX52;'
        f'UID=R520MRHA;'
        f'PWD=RH644707!;'
    )
    cursor = conn.cursor()
    cursor.execute(PICK_ANOMALIES)
    result = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

        # Convertir les lignes en liste de listes
    data = [[str(item) if item is not None else "" for item in row] for row in result]
    print(f"Nombre de lignes récupérées : {len(data)}")  # Ajout pour débogage
    # Créer un DataFrame pandas
    global df 
    df = pd.DataFrame(data, columns=headers)
 
except pyodbc.Error as e:
    print(e)

# # PostgreSQL connection details
db_username = 'Usolvix'
db_password = '1234'
db_host = '10.49.0.179'  # or your host IP
db_port = '5432'       # default port for PostgreSQL
db_name = 'Solvix'
table_name = 'anomalies'

# Create connection to PostgreSQL
connection_string = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)

# Create table based on DataFrame columns
def create_table_from_df(df, table_name):
    # Get column names and types from DataFrame
    column_types = []
    for col, dtype in zip(df.columns, df.dtypes):
        if "int" in str(dtype):
            sql_type = "INTEGER"
        elif "float" in str(dtype):
            sql_type = "FLOAT"
        elif "object" in str(dtype):  # Assume strings for object types
            sql_type = "TEXT"
        elif "datetime" in str(dtype):
            sql_type = "TIMESTAMP"
        else:
            sql_type = "TEXT"  # Default to TEXT for unknown types
        column_types.append(f"{col} {sql_type}")
    
    # Create the SQL query for table creation
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(column_types)}
    )
    """
    
    try:
        # Execute the table creation query
        SolviXcursor.execute(text(create_table_query))
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")

# Create the table
create_table_from_df(df, table_name)

# Insert data into the newly created table
try:
    df.to_sql(table_name, SolviXconn, if_exists='append', index=False)  # Insert data into the table
    print(f"Data inserted successfully into table '{table_name}'.")
except Exception as e:
    print(f"Error inserting data into table '{table_name}': {e}")

# Confirm the data was inserted
try:
   
    result = SolviXcursor.execute(text(f"SELECT * FROM {table_name}"))
    for row in result:
        print(row)
except Exception as e:
    print(f"Error executing query: {e}")
