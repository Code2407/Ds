import pandas as pd
import sqlite3 as sq

print("Umang,26")
AB = 'student.csv'

InputData = pd.read_csv(AB)
print(InputData)

ProcessData = InputData

OutputData = ProcessData

SOutputFileName = 'Zaidmetpooja.db'
sOutputTable = 'Employee'
conn = sq.connect(SOutputFileName)
OutputData.to_sql(sOutputTable, conn, if_exists="replace")
print('Done')
