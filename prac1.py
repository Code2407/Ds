import pandas as pd
print("Umang,26")
sInputFileName='student.csv'
InputData=pd.read_csv(sInputFileName)
print("Input data value=============================")
print(InputData)
ProcessData=InputData

#Remove the Column
ProcessData.drop('email',axis=1,inplace=True)
ProcessData.drop('date',axis=1,inplace=True)
print("Process data value=============================")

#Rename the Column
ProcessData.rename(columns={'name':'Stud_name'},inplace=True)
ProcessData.rename(columns={'phone':'Stud_Phone'},inplace=True)
print(ProcessData)
OutputData=ProcessData
OutputData.to_csv('student1.csv')
print('Done')