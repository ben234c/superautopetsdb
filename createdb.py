import mysql.connector
import pandas as pd
import pypyodbc as odbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


# connect to db, replace strings with your credentials
mydb = mysql.connector.connect(
    host = 'host',
    user = 'user',
    password = 'password'
)

# create db and table
with open('createdb.sql', 'r') as f:
    with mydb.cursor() as cursor:
        cursor.execute(f.read(), multi=True)

mydbcursor = mydb.cursor()

# cant afford excel, use odf engine to allow .ods files to be used
df = pd.read_excel('SuperAutoPets.ods',sheet_name='Pets', engine='odf')

# fill any empty spaces
df = df.fillna(0)

# excel files store numbers as floats, so convert to int
df['Tier'] = df['Tier'].astype(int)
df['Attack'] = df['Attack'].astype(int)
df['Health'] = df['Health'].astype(int)

print(df)






# create tables
# if sap database does not exist, create it and put in runs and turns table

# get data from excel to sql db (just to create, implement updating later)
