import psycopg2
import pandas as pd
from DB.database import connect_to_db

def run_query(query):
    conn = connect_to_db()
    if not conn:
        print("error connecting to database")

    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df);
    return df
