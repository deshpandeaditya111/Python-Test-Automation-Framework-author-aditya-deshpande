import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from _overlapped import NULL

# df is data frame
class ExcelCom():

 def setFilePath(self,Filepath, SheetName):
     global df
     df=pd.read_excel(Filepath, sheetname=SheetName)
     

 def getRowContains(self,TestCaseName, ColumnName):
     print(df)
     for i in df.index:
         a= df[ColumnName][i]
         if(a==TestCaseName):
             break
     return i
     
 def getCellData(self, RowNum, ColNum):
     var=df.iloc[RowNum,ColNum]
     return var
 