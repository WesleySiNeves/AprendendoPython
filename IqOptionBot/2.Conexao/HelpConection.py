from iqoptionapi.stable_api import  IQ_Option
import time
import pandas as pd
import json


user ='wesley.si.neves@hotmail.com';
password  ='96086512'
API = IQ_Option(user,password)
# API.set_max_reconnect(5);
# API.change_balance('PRACTICE') # PRACTICE(treinamento) REAL (real)

while True:
    if(API.check_connect() ==False):
        print("Tentando conectar")
        API.reconnect()
    
    else:
        print("Api conectada com sucesso")
        break;
    
    time.sleep(1)
        
API.connect()        


def get_perfil():
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))
    
    return perfil


print(get_perfil())


        
    

