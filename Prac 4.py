import pandas as pd
import sqlite3 as sq

print("Umang,26")
sInputFileName = 'Zaidmetpooja.db'
sInputTable = 'Employee'

# creating connection
conn = sq.connect(sInputFileName)

sSql = 'select * from ' + sInputTable + ';'
InputData = pd.read_sql_query(sSql, conn)
print(InputData)

ProcessData = InputData

# Remove the Column
# ProcessData.drop('email', axis=1, inplace=True)
print("Process data value=============================")
print(InputData)

# Rename the Column
ProcessData.rename(columns={'name': 'Fullname'}, inplace=True)
ProcessData.rename(columns={'phone': 'PhoneNumber'}, inplace=True)
ProcessData.rename(columns={'email': 'Email Address'}, inplace=True)
print(ProcessData)

OutputData = ProcessData
OutputData.to_csv('Umang.csv')

print('Done')
