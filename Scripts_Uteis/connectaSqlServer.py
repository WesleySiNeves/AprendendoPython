
import pandas as pd
import pyodbc as conectDb
import getArquivos as get
import os as  listdir
import xlrd as Excel

#Declaração de variaveis




sourceFile = "D:\VersionCode\Python\dados"
    


conn = conectDb.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=rgdev-sqlsrv-dev01.database.windows.net;"
                      "Database=15.2-implantaModificado;"
                      "uid=implantadev01;"
                      "pwd=Impl@ntadev01;")



cursor = conn.cursor()
cursor.execute("SELECT top 1 * FROM sys.tables")

for row in cursor:
    print(row)
