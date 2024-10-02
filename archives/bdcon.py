import psycopg2
from psycopg2 import sql


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

    # # Execute a simple SQL query to verify connection
    # SolviXcursor.execute("SELECT version();")

    # # Fetch and print the result of the query
    # db_version = SolviXcursor.fetchone()
    # print(f"PostgreSQL Database version: {db_version}")

except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

