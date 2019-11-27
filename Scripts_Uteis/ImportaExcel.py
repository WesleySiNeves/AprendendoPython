
import pandas as pd
import pyodbc as conectDb
import getArquivos as get
import os as  listdir
import xlrd as Excel
import time




#Declaração de variaveis

serverName ="rgdev-sqlsrv-dev01.database.windows.net"
Database = "15.2-implantaModificado"
Trusted_Connection ="Yes"
User ="implantadev01"
Pass ="Impl@ntadev01"


sourceFile = "D:\VersionCode\Python\dados"


start_time = time.time()
connStr = conectDb.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=rgdev-sqlsrv-dev01.database.windows.net;"
                      "Database=15.2-implantaModificado;"
                      "uid=implantadev01;"
                      "pwd=Impl@ntadev01;")




filenames = get.find_filenames(sourceFile,".xls")

cursor = connStr.cursor()

for nameFile in filenames:
    strfile = listdir.path.join(sourceFile, nameFile)

    workbook = Excel.open_workbook(strfile)

    #for nameScheet  in workbook.sheet_names():
    #for nameScheet  in workbook.get_sheets():

    dados = pd.read_excel(strfile,sheet_name ="Profissional")  
    
    dados.fillna({"CPFCNPJ":""})

    for index,row in dados.iterrows():
        cursor.execute("INSERT INTO dbo.profissional(CPFCNPJ,NOME,REGISTRO,SITUACAOREGISTRO) values (?, ?,?,?)",
        row['CPFCNPJ'], 
        row['NOME'], 
        row['REGISTRO'],
        row['SITUAÇÃO REGISTRO'])
    
connStr.commit()
cursor.close()
connStr.close()    

print("%s seconds ---" % (time.time() - start_time))            


