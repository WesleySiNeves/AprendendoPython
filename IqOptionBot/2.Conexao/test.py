from iqoptionapi.stable_api import  IQ_Option
import time
import pandas as pd
import json
from datetime import datetime  
from datetime import timedelta 
from dateutil import tz
import schedule as tarefa
import threading 




def time_convert(x):
    hora =datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo = tz.gettz('GMT'))

    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))

user ='wesley.si.neves@hotmail.com';
password  ='96086512'

def get_Api(user,password):
    API = IQ_Option(user,password)
    return API

API = get_Api(user,password)


while True:
    if(API.check_connect() ==False):
        print("Tentando conectar")
        API.reconnect()
    
    else:
        print("Api conectada com sucesso")
        break;
    
    time.sleep(1)
        
API.connect()  


controlador = {'count': 0}


def CALL(par,entrada,horarioOperacao,tempoOperacao =1,is_digital = 0, data =None):
    # par ='EURUSD-OTC'
  
    data['count'] += 1
    tentativasMaxima =3
    tentativa =1

    status = -1
    id = 0
    direcao ='call'
    
    horaLimite = (datetime.strptime(horarioOperacao, '%H:%M:%S') + timedelta(seconds=4))


    mytime = datetime.strptime(str(horaLimite),'%Y-%d-%m %H:%M:%S').time() 
    mydatetime = datetime.combine(datetime.today(), mytime)

    if(datetime.now() > mydatetime):
        print(' Compra Cancelada por atraso na execução em: Hora atual:',str(datetime.now()), ' Hora que o job deveria ser executado:',mydatetime)
        return;
        

    print('Job:',data['count']);
    while(tentativa <= tentativasMaxima):
        
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
            print(' Compra realizada em: Hora',str(datetime.now()))
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        if(status):
            result  =API.check_win_v3(id)
            if(result > 0):
                print('resultado:Win', 'Valor:',str(round(result,2)))
                break
            else:
                print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                tentativa +=1
                entrada  += entrada
        else:
            print('Erro ao comprar a moeda ',par, 'Hora:',str(datetime.now()),'Mensagem:',id)
            break
            


def CALL_StopLoss(par,entrada,tempoOperacao =1,is_digital = 0):
    # par ='EURUSD-OTC'
    tentativasMaxima =3
    tentativa =1

    status = -1
    id = 0
    direcao ='call'
    isWin = False

    while(tentativa <= tentativasMaxima):
        
        if(isWin):
            entrada =2

        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        print(status)
        result  =API.check_win_v3(id)
        if(result > 0):
            isWin = True
            print('resultado:Win', 'Valor:',str(round(result,2)))
        else:
            print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
            tentativa +=1
            entrada  += entrada
            isWin = False


def PUT(par,entrada,horarioOperacao,tempoOperacao,is_digital = 0, data =None,horarioLimite =''):
    # par ='EURUSD-OTC'
    tentativasMaxima =3
    tentativa =1

    status = -1
    id = 0
    direcao ='put'
    data['count'] += 1
    
    horaLimite = (datetime.strptime(horarioOperacao, '%H:%M:%S') + timedelta(seconds=4))


    mytime = datetime.strptime(str(horaLimite),'%Y-%d-%m %H:%M:%S').time() 
    mydatetime = datetime.combine(datetime.today(), mytime)

    if(datetime.now() > mydatetime):
        print(' Compra Cancelada por atraso na execução em: Hora atual:',str(datetime.now()), ' Hora que o job deveria ser executado:',mydatetime)
        return;
    
    
    print('Job:',data['count']);
    while(tentativa <= tentativasMaxima):
        
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
            print('Compra realizada em: Hora',str(datetime.now()))
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        if(status):
            result  =API.check_win_v3(id)
            if(result > 0):
                print('resultado:Win', 'Valor:',str(round(result,2)))
                break
            else:
                print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                tentativa +=1
                entrada  += entrada
        else:
            print('Erro ao comprar a moeda ',par, 'Hora:',str(datetime.now()),'Mensagem:',id)
            break
            
   

def get_balance():
    return API.get_balance()
   
def coding():
    print('execution at:', time_convert(time.time()))



def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    

      
tarefa.every(10).seconds.do(coding)
             


    
tarefa.every().day.at('01:06:57').do(CALL,par ='AUDUSD',entrada=10,horarioOperacao ='01:06:57', tempoOperacao=1, is_digital=0,data=controlador); #;00:07-CALL	M1-
tarefa.every().day.at('00:27:57').do(CALL,par ='GBPJPY',entrada=10,horarioOperacao ='00:27:57', tempoOperacao=1, is_digital=0,data=controlador); #;00:27-CALL	M1-
tarefa.every().day.at('02:57:57').do(CALL,par ='AUDUSD',entrada=10,horarioOperacao ='02:57:57', tempoOperacao=1, is_digital=0,data=controlador); #;02:57-CALL	M1-
tarefa.every().day.at('03:32:57').do(PUT,par ='GBPJPY', entrada=10,horarioOperacao ='03:32:57', tempoOperacao=1, is_digital=0,data=controlador); #;03:32-PUT	M1-
tarefa.every().day.at('04:42:57').do(CALL,par ='GBPCAD',entrada=10,horarioOperacao ='04:42:57', tempoOperacao=1, is_digital=0,data=controlador); #;04:42-CALL	M1-
tarefa.every().day.at('05:05:57').do(PUT,par ='GBPJPY', entrada=10,horarioOperacao ='05:05:57', tempoOperacao=1, is_digital=0,data=controlador); #;05:05-PUT	M1-
tarefa.every().day.at('05:52:57').do(PUT,par ='GBPNZD', entrada=10,horarioOperacao ='05:52:57', tempoOperacao=1, is_digital=0,data=controlador); #;05:52-PUT	M1-
tarefa.every().day.at('06:05:57').do(PUT,par ='GBPJPY', entrada=10,horarioOperacao ='06:05:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:05-PUT	M1-
tarefa.every().day.at('06:07:57').do(PUT,par ='GBPJPY', entrada=10,horarioOperacao ='06:07:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:07-PUT	M1-
tarefa.every().day.at('06:37:57').do(PUT,par ='USDCAD', entrada=10,horarioOperacao ='06:37:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:37-PUT	M1-
tarefa.every().day.at('06:42:57').do(PUT,par ='AUDCAD', entrada=10,horarioOperacao ='06:42:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:42-PUT	M1-
tarefa.every().day.at('06:42:57').do(PUT,par ='EURUSD', entrada=10,horarioOperacao ='06:42:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:42-PUT	M1-
tarefa.every().day.at('06:47:57').do(PUT,par ='EURAUD', entrada=10,horarioOperacao ='06:47:57', tempoOperacao=1, is_digital=0,data=controlador); #;06:47-PUT	M1-





tarefa.every().day.at('05:50:57').do(PUT,par ='GBPNZD',entrada=10,horarioOperacao ='05:50:57', tempoOperacao=5, is_digital=0,data=controlador);#05:50 #-PUT M5-
tarefa.every().day.at('06:05:57').do(PUT,par ='GBPJPY',entrada=10,horarioOperacao ='06:05:57', tempoOperacao=5, is_digital=0,data=controlador);#06:05 #-PUT M5-
tarefa.every().day.at('06:35:57').do(PUT,par ='USDCAD',entrada=10,horarioOperacao ='06:35:57', tempoOperacao=5, is_digital=0,data=controlador);#06:35 #-PUT M5-
tarefa.every().day.at('06:40:57').do(PUT,par ='AUDCAD',entrada=10,horarioOperacao ='06:40:57', tempoOperacao=5, is_digital=0,data=controlador);#06:40 #-PUT M5-
tarefa.every().day.at('06:40:57').do(PUT,par ='EURUSD',entrada=10,horarioOperacao ='06:40:57', tempoOperacao=5, is_digital=0,data=controlador);#06:40 #-PUT M5-
tarefa.every().day.at('06:45:57').do(PUT,par ='EURAUD',entrada=10,horarioOperacao ='06:45:57', tempoOperacao=5, is_digital=0,data=controlador);#06:45 #          

    
        
while True:
    tarefa.run_pending()
    time.sleep(1)
    if(controlador['count'] >=2):
        tarefa.clear();
        break

print('Fim do Robo')