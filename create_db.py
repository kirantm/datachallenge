import sqlite3
from sqlite3 import Error

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        #c.execute("DROP TABLE IF EXISTS RAW")
        #c.execute("DROP TABLE IF EXISTS CLEAN")
        c.execute('''
            CREATE TABLE IF NOT EXISTS RAW
            ([First_Name], [Last_Name], [Address], [Email], [DOB], [Ethinicity], [Education], [Age])
            ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS CLEAN
            ([First_Name] TEXT, [Last_Name] TEXT, [Address] TEXT, [Email] TEXT, [DOB] INTEGER, [Ethinicity] TEXT, [Education] TEXT, [Age] INTEGER)
            ''')

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
   create_conn(r"sqlite_db\sqlite3.db")