from iqoptionapi.stable_api import  IQ_Option
import time
import pandas as pd
import json
from datetime import datetime
from dateutil import tz
import schedule as tarefa


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


def Put(par,entrada,tempoOperacao =1,is_digital = 0):
    # par ='EURUSD-OTC'
    tentativasMaxima =3
    tentativa =1

    status = -1
    id = 0
    direcao ='put'
    

    while(tentativa < tentativasMaxima):
        
        if(id != -1):
            result  =API.check_win_v3(id)
            if(result > 0):
                print('resultado:Win', 'Valor:',str(round(result,2)))
                break
        
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        if(id != -1):
            result  =API.check_win_v3(id)
            if(result > 0):
                print('resultado:Win', 'Valor:',str(round(result,2)))
                break
            else:
                print('resultado:Loss', 'Valor:',str(round(result * -1,2)))
                tentativa +=1
                entrada  += entrada
                if(is_digital ==0):
                    status,id = API.buy(entrada,par,direcao,tempoOperacao)
                else:
                    status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
                time.sleep(1)
                
                
def Call(par,entrada,tempoOperacao =1,is_digital = 0):
    # par ='EURUSD-OTC'
    tentativasMaxima =3
    tentativa =1

    status = -1
    id = 0
    direcao ='call'

    while(tentativa <= tentativasMaxima):
        
        if(is_digital ==0):
            status,id = API.buy(entrada,par,direcao,tempoOperacao)
        else:
            status,id = API.buy_digital_spot(entrada,par,direcao,tempoOperacao)
        
        result  =API.check_win_v3(id)
        if(result > 0):
            print('resultado:Win', 'Valor:',str(round(result,2)))
            break
        else:
            print('resultado:Loss', 'Valor:',str(round((result * -1),2)))
            tentativa +=1
            entrada  += entrada
                

                
Call('EURUSD-OTC',2,1,0)                