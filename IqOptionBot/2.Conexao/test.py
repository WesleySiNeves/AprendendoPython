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

def get_balance():
    return API.get_balance()


controlador = {'count': 0, 'stoploss': 0}

controlador['stoploss'] =  round(get_balance() * 0.20,2)






BalanceMode = 'REAL'  # REAL(Vera) / PRACTICE 
API.change_balance(BalanceMode)
print('Saldo Inicial', str(get_balance())) 


stop_loss = get_balance() * 0.20
stop_loss

def CALL(par,entrada,horarioOperacao,tempoOperacao =1,is_digital = 0, data =None):
    
    direcao ='call'

    data['count'] += 1
    
    
    tentativasMaxima =3
    tentativa =1
    status = -1
    id = 0

    horaLimite = (datetime.strptime(horarioOperacao, '%H:%M:%S') + timedelta(seconds=4))
    mytime = datetime.strptime(str(horaLimite),'%Y-%d-%m %H:%M:%S').time() 
    mydatetime = datetime.combine(datetime.today(), mytime)

    if(datetime.now() > mydatetime):
        print(' Compra Cancelada atraso na execução em: Hora atual:',str(datetime.now()), ' Hora que o job deveria ser executado:',mydatetime)
        return;


    print('Job:',data['count'],' Moeda:',par);
    while(tentativa <= tentativasMaxima and data['stoploss'] > 0):
        print('Compra realizada em: Hora',str(datetime.now()))
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        if(status):
            result  =API.check_win_v3(id)
            
            if(tentativa == 1):
                if(result == 0): #doji
                    print('resultado:Doji na primeira vela', 'Valor:',str(round(result,2)))
                    isWin = False
                    tentativa +=1
                    break;
                if(result > 0):
                    print('resultado:Win', 'Valor:',str(round(result,2)))
                    break;
                if(result < 0):
                    print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                    tentativa +=1
                    data['stoploss'] -= result;
                    entrada  += entrada
                    break;
            
            if(tentativa == 2):
                if(result == 0): #doji
                    print('resultado:Doji na primeira vela', 'Valor:',str(round(result,2)))
                    isWin = False
                    tentativa +=1
                    entrada  += entrada
                    break;
                if(result > 0):
                    print('resultado:Win', 'Valor:',str(round(result,2)))
                    isWin = True
                    break;
                if(result < 0):
                    print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                    tentativa +=1
                    data['stoploss'] -= result;
                    isWin = False
            
            else:
                print('Erro ao comprar a moeda ',par, 'Hora:',str(datetime.now()),'Mensagem:',id)
                break



def PUT(par,entrada,horarioOperacao,tempoOperacao,is_digital = 0, data =None,horarioLimite =''):
    # par ='EURUSD-OTC'
    direcao ='put'

    data['count'] += 1
    tentativasMaxima =3
    tentativa =1
    status = -1
    id = 0

    horaLimite = (datetime.strptime(horarioOperacao, '%H:%M:%S') + timedelta(seconds=4))
    mytime = datetime.strptime(str(horaLimite),'%Y-%d-%m %H:%M:%S').time() 
    mydatetime = datetime.combine(datetime.today(), mytime)

    if(datetime.now() > mydatetime):
        print(' Compra Cancelada atraso na execução em: Hora atual:',str(datetime.now()), ' Hora que o job deveria ser executado:',mydatetime)
        return;

    

    print('Job:',data['count'],' Moeda:',par);
    while(tentativa <= tentativasMaxima and data['stoploss'] > 0):
        print('Compra realizada em: Hora',str(datetime.now()))
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        if(status):
            result  =API.check_win_v3(id)
            
            if(tentativa == 1):
                if(result == 0): #doji
                    print('resultado:Doji na primeira vela', 'Valor:',str(round(result,2)))
                    isWin = False
                    tentativa +=1
                    break;
                if(result > 0):
                    print('resultado:Win', 'Valor:',str(round(result,2)))
                    break;
                if(result < 0):
                    print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                    tentativa +=1
                    entrada  += entrada
                    data['stoploss'] -= result;
                    break;
            
            if(tentativa == 2):
                if(result == 0): #doji
                    print('resultado:Doji na primeira vela', 'Valor:',str(round(result,2)))
                    isWin = False
                    tentativa +=1
                    entrada  += entrada
                    break;
                if(result > 0):
                    print('resultado:Win', 'Valor:',str(round(result,2)))
                    isWin = True
                    break;
                if(result < 0):
                    print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
                    tentativa +=1
                    data['stoploss'] -= result;
                    isWin = False
            
            else:
                print('Erro ao comprar a moeda ',par, 'Hora:',str(datetime.now()),'Mensagem:',id)
                break
 
   
def coding():
    print('execution at:', time_convert(time.time()))



def get_moedas_abertas(tipo ='turbo'):
        moedas = API.get_all_open_time()
        # lista = []
        # dicionario = {}
        # tupla = ()
        # turbo/binary
        retorno = []

        for paridade in moedas['turbo']:
            if( moedas['turbo'][paridade]['open'] ==True):
                retorno.append(paridade)
        
        return retorno
    
    

      
tarefa.every(30).seconds.do(coding)


tarefa.every().day.at('00:35:57').do(CALL ,par ='AUDUSD',entrada=2,horarioOperacao ='00:35:57', tempoOperacao=1, is_digital=0,data=controlador);#;00:36-CALL    M1-
tarefa.every().day.at('02:35:57').do(CALL ,par ='GBPAUD',entrada=2,horarioOperacao ='02:35:57', tempoOperacao=1, is_digital=0,data=controlador);#;02:36-CALL    M1-
tarefa.every().day.at('02:40:57').do(PUT  ,par ='EURGBP',entrada=2,horarioOperacao ='02:40:57', tempoOperacao=1, is_digital=0,data=controlador);#;02:41-PUT     M1-
tarefa.every().day.at('02:55:57').do(PUT  ,par ='CADCHF',entrada=2,horarioOperacao ='02:55:57', tempoOperacao=1, is_digital=0,data=controlador);#;02:56-PUT     M1-
tarefa.every().day.at('03:00:57').do(PUT  ,par ='CADCHF',entrada=2,horarioOperacao ='03:00:57', tempoOperacao=1, is_digital=0,data=controlador);#;03:01-PUT     M1-
tarefa.every().day.at('04:45:57').do(CALL ,par ='EURJPY',entrada=2,horarioOperacao ='04:45:57', tempoOperacao=1, is_digital=0,data=controlador);#;04:46-CALL    M1-
tarefa.every().day.at('04:50:57').do(CALL ,par ='AUDNZD',entrada=2,horarioOperacao ='04:50:57', tempoOperacao=1, is_digital=0,data=controlador);#;04:51-CALL    M1-
tarefa.every().day.at('05:00:57').do(CALL ,par ='EURUSD',entrada=2,horarioOperacao ='05:00:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:01-CALL    M1-
tarefa.every().day.at('05:05:57').do(CALL ,par ='EURCHF',entrada=2,horarioOperacao ='05:05:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:06-CALL    M1-
tarefa.every().day.at('05:10:57').do(CALL ,par ='EURCHF',entrada=2,horarioOperacao ='05:10:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:11-CALL    M1-
tarefa.every().day.at('05:20:57').do(CALL ,par ='AUDCAD',entrada=2,horarioOperacao ='05:20:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:21-CALL    M1-
tarefa.every().day.at('05:25:57').do(CALL ,par ='AUDUSD',entrada=2,horarioOperacao ='05:25:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:26-CALL    M1-
tarefa.every().day.at('05:30:57').do(PUT  ,par ='USDCAD',entrada=2,horarioOperacao ='05:30:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:31-PUT     M1-
tarefa.every().day.at('05:40:57').do(PUT  ,par ='AUDNZD',entrada=2,horarioOperacao ='05:40:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:41-PUT     M1-
tarefa.every().day.at('05:55:57').do(CALL ,par ='GBPNZD',entrada=2,horarioOperacao ='05:55:57', tempoOperacao=1, is_digital=0,data=controlador);#;05:56-CALL    M1-
tarefa.every().day.at('06:10:57').do(PUT  ,par ='GBPCHF',entrada=2,horarioOperacao ='06:10:57', tempoOperacao=1, is_digital=0,data=controlador);#;06:11-PUT     M1-
tarefa.every().day.at('06:15:57').do(PUT  ,par ='GBPNZD',entrada=2,horarioOperacao ='06:15:57', tempoOperacao=1, is_digital=0,data=controlador);#;06:16-PUT     M1-
tarefa.every().day.at('06:50:57').do(PUT  ,par ='CADCHF',entrada=2,horarioOperacao ='06:50:57', tempoOperacao=1, is_digital=0,data=controlador);#;06:51-PUT     M1-
tarefa.every().day.at('07:00:57').do(PUT  ,par ='AUDNZD',entrada=2,horarioOperacao ='07:00:57', tempoOperacao=1, is_digital=0,data=controlador);#;07:01-PUT     M1-
tarefa.every().day.at('07:05:57').do(CALL ,par ='USDJPY',entrada=2,horarioOperacao ='07:05:57', tempoOperacao=1, is_digital=0,data=controlador);#;07:06-CALL    M1-
tarefa.every().day.at('07:25:57').do(CALL ,par ='AUDCAD',entrada=2,horarioOperacao ='07:25:57', tempoOperacao=1, is_digital=0,data=controlador);#;07:26-CALL    M1-
tarefa.every().day.at('07:50:57').do(CALL ,par ='GBPNZD',entrada=2,horarioOperacao ='07:50:57', tempoOperacao=1, is_digital=0,data=controlador);#;07:51-CALL    M1-
tarefa.every().day.at('07:55:57').do(CALL ,par ='GBPNZD',entrada=2,horarioOperacao ='07:55:57', tempoOperacao=1, is_digital=0,data=controlador);#;07:56-CALL    M1-


tarefa.every().day.at('00:34:57').do(PUT  ,par ='USDJPY',entrada=2,horarioOperacao ='00:34:57', tempoOperacao=5, is_digital=0,data=controlador);#;00:35-PUT    M5-
tarefa.every().day.at('00:59:57').do(CALL ,par ='AUDUSD',entrada=2,horarioOperacao ='00:59:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:00-CALL   M5-
tarefa.every().day.at('01:14:57').do(PUT  ,par ='EURUSD',entrada=2,horarioOperacao ='01:14:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:15-PUT    M5-
tarefa.every().day.at('01:19:57').do(CALL ,par ='EURJPY',entrada=2,horarioOperacao ='01:19:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:20-CALL   M5-
tarefa.every().day.at('01:24:57').do(CALL ,par ='EURJPY',entrada=2,horarioOperacao ='01:24:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:25-CALL   M5-
tarefa.every().day.at('01:39:57').do(PUT  ,par ='AUDNZD',entrada=2,horarioOperacao ='01:39:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:40-PUT    M5-
tarefa.every().day.at('01:54:57').do(PUT  ,par ='AUDCHF',entrada=2,horarioOperacao ='01:54:57', tempoOperacao=5, is_digital=0,data=controlador);#;01:55-PUT    M5-
tarefa.every().day.at('02:09:57').do(CALL ,par ='USDJPY',entrada=2,horarioOperacao ='02:09:57', tempoOperacao=5, is_digital=0,data=controlador);#;02:10-CALL   M5-
tarefa.every().day.at('02:14:57').do(PUT  ,par ='AUDCHF',entrada=2,horarioOperacao ='02:14:57', tempoOperacao=5, is_digital=0,data=controlador);#;02:15-PUT    M5-
tarefa.every().day.at('02:24:57').do(CALL ,par ='GBPAUD',entrada=2,horarioOperacao ='02:24:57', tempoOperacao=5, is_digital=0,data=controlador);#;02:25-CALL   M5-
tarefa.every().day.at('02:34:57').do(CALL ,par ='GBPAUD',entrada=2,horarioOperacao ='02:34:57', tempoOperacao=5, is_digital=0,data=controlador);#;02:35-CALL   M5-
tarefa.every().day.at('02:54:57').do(PUT  ,par ='CADCHF',entrada=2,horarioOperacao ='02:54:57', tempoOperacao=5, is_digital=0,data=controlador);#;02:55-PUT    M5-
tarefa.every().day.at('02:59:57').do(PUT  ,par ='USDJPY',entrada=2,horarioOperacao ='02:59:57', tempoOperacao=5, is_digital=0,data=controlador);#;03:00-PUT    M5-
tarefa.every().day.at('03:19:57').do(CALL ,par ='CADCHF',entrada=2,horarioOperacao ='03:19:57', tempoOperacao=5, is_digital=0,data=controlador);#;03:20-CALL   M5-
tarefa.every().day.at('04:39:57').do(CALL ,par ='AUDNZD',entrada=2,horarioOperacao ='04:39:57', tempoOperacao=5, is_digital=0,data=controlador);#;04:40-CALL   M5-
tarefa.every().day.at('04:44:57').do(CALL ,par ='AUDNZD',entrada=2,horarioOperacao ='04:44:57', tempoOperacao=5, is_digital=0,data=controlador);#;04:45-CALL   M5-
tarefa.every().day.at('04:49:57').do(CALL ,par ='EURJPY',entrada=2,horarioOperacao ='04:49:57', tempoOperacao=5, is_digital=0,data=controlador);#;04:50-CALL   M5-
tarefa.every().day.at('04:59:57').do(CALL ,par ='EURUSD',entrada=2,horarioOperacao ='04:59:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:00-CALL   M5-
tarefa.every().day.at('05:09:57').do(CALL ,par ='EURNZD',entrada=2,horarioOperacao ='05:09:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:10-CALL   M5-
tarefa.every().day.at('05:19:57').do(CALL ,par ='AUDCAD',entrada=2,horarioOperacao ='05:19:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:20-CALL   M5-
tarefa.every().day.at('05:24:57').do(PUT  ,par ='USDCAD',entrada=2,horarioOperacao ='05:24:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:25-PUT    M5-
tarefa.every().day.at('05:34:57').do(PUT  ,par ='AUDCHF',entrada=2,horarioOperacao ='05:34:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:35-PUT    M5-
tarefa.every().day.at('05:39:57').do(PUT  ,par ='CADCHF',entrada=2,horarioOperacao ='05:39:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:40-PUT    M5-
tarefa.every().day.at('05:44:57').do(PUT  ,par ='CADJPY',entrada=2,horarioOperacao ='05:44:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:45-PUT    M5-
tarefa.every().day.at('05:49:57').do(PUT  ,par ='EURJPY',entrada=2,horarioOperacao ='05:49:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:50-PUT    M5-
tarefa.every().day.at('05:59:57').do(PUT  ,par ='AUDUSD',entrada=2,horarioOperacao ='05:59:57', tempoOperacao=5, is_digital=0,data=controlador);#;05:50-PUT    M5-
tarefa.every().day.at('06:04:57').do(CALL ,par ='EURNZD',entrada=2,horarioOperacao ='06:04:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:05-CALL   M5-
tarefa.every().day.at('06:09:57').do(PUT  ,par ='AUDJPY',entrada=2,horarioOperacao ='06:09:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:10-PUT    M5-
tarefa.every().day.at('06:14:57').do(PUT  ,par ='GBPNZD',entrada=2,horarioOperacao ='06:14:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:15-PUT    M5-
tarefa.every().day.at('06:19:57').do(PUT  ,par ='EURUSD',entrada=2,horarioOperacao ='06:19:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:20-PUT    M5-
tarefa.every().day.at('06:24:57').do(PUT  ,par ='EURUSD',entrada=2,horarioOperacao ='06:24:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:25-PUT    M5-
tarefa.every().day.at('06:29:57').do(PUT  ,par ='GBPJPY',entrada=2,horarioOperacao ='06:29:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:30-PUT    M5-
tarefa.every().day.at('06:34:57').do(PUT  ,par ='GBPUSD',entrada=2,horarioOperacao ='06:34:57', tempoOperacao=5, is_digital=0,data=controlador);#;06:35-PUT    M5-
tarefa.every().day.at('07:29:57').do(CALL ,par ='AUDCAD',entrada=2,horarioOperacao ='07:29:57', tempoOperacao=5, is_digital=0,data=controlador);#;07:30-CALL   M5-
tarefa.every().day.at('07:34:57').do(PUT  ,par ='USDCHF',entrada=2,horarioOperacao ='07:34:57', tempoOperacao=5, is_digital=0,data=controlador);#;07:35-PUT    M5-
tarefa.every().day.at('07:49:57').do(PUT  ,par ='USDCAD',entrada=2,horarioOperacao ='07:49:57', tempoOperacao=5, is_digital=0,data=controlador);#;07:50-PUT    M5-



while True:
    tarefa.run_pending()
    time.sleep(1)
    if(controlador['count'] > len(tarefa.jobs)):
        tarefa.clear();
        break;

print('Fim do Robo')