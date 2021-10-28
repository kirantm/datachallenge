import csv
import datetime
import numpy as np
import random
import pandas as pd
import sqlite3
from sqlite3 import Error


df = pd.read_csv(r"C:\Users\Kiran\Desktop\SparkFishCodingChallenge\Raw.csv")

df['Education'] = df['Education'].apply(lambda v: random.choice(["High School", "Associate", "Bachelor's", "Master's", "Doctorate"]))

df['DOB'] = np.random.choice(pd.date_range('1961-01-01','2003-01-01'), len(df))

df['Ethnicity'] = df['Ethnicity'].apply(lambda v: random.choice(['White','Black','Asian','Unknown','Native American']))

today = pd.to_datetime('today')
df['Age']=today.year-df['DOB'].dt.year

df.to_csv('Raw_Data.csv', index = False)

with open('Raw_Data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data_list = list(reader)

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
    create_conn(r"C:\Users\Kiran\Desktop\SparkFish Coding Challenge\sqlite_db\sqlite3.db")