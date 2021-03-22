from iqoptionapi.stable_api import  IQ_Option
import time
import pandas as pd
import json
from datetime import datetime
from dateutil import tz
import schedule as tarefa


class HelperApi():
    
    def __init__(self,user,senha):
        self.User =user
        self.Senha =senha
        self.API =""
        self.TentativasConexao =0
        self.ListaMoedas =("EURUSD")
        self.TempoEmMinutos =1
        self.ListaTimes =(1,2,5)
        self.Moeda =""
        
    
    def get_API(self):
        API = IQ_Option(self.User,self.Senha)
        
    def get_OnConnection(self):
        while True:
            if(self.API.check_connect() ==False):
                print("Tentando conectar")
                self.TentativasConexao +=1
                self.API.reconnect()
    
            else:
                print("Api conectada com sucesso")
                break;
            time.sleep(1)
        
            self.API.connect() 
        
        
        
    def get_Saldo(self):
        return self.API.get_balance()
    
    def time_convert(self,x):
        hora =datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
        hora = hora.replace(tzinfo = tz.gettz('GMT'))
        return str(hora.astimezone(tz.gettz('America/Sao Paulo')))
    
    def get_perfil(self):
        perfil = json.loads(json.dumps(self.API.get_profile_ansyc()))
    
        return perfil
    
    
    def get_tempo_da_vela(self):
        fator_multiplicacao = 60
        
        return self.TempoEmMinutos * fator_multiplicacao
        
    
    def get_velas(self,moeda,quantidades_velas) :
        velas = API.get_candles(moeda,(self.TempoEmMinutos * 60) ,quantidades_velas,time.time())
        
        return velas
    
    def get_humor_par_binaria(self,moeda):
        API.start_mood_stream(moeda)
        while(True):
            result = API.get_traders_mood(moeda)
            print(int(100 * round(result,2)))
            time.sleep(1)
        
        API.stop_mood_stream(moeda)
     
    
    def get_moedas_abertas(self,tipo ='turbo'):
        moedas = self.API.get_all_open_time()
        # lista = []
        # dicionario = {}
        # tupla = ()
        # turbo/binary
        retorno = []

        for paridade in moedas['turbo']:
            if( moedas['turbo'][paridade]['open'] ==True):
                retorno.append(paridade)
        
        return retorno
    
    
    def get_payout(self,par,tipo,tempovela =1):
    
        if(tipo  =='turbo'):
            result = API.get_all_profit()
            return ('turbo',(100 * result[par][tipo]))
        elif(tipo =='bynary'):
            API.subscribe_strike_list(par,tempovela)
            while True:
                d = API.get_digital_current_profit(par,tempovela)
                if(d != False):
                    d = int(d)
                    break;
                time.sleep(1)
            API.unsubscribe_strike_list(par,tempovela)
            return ('bynary',(d))
        
    
    def get_historico_jogadas(self,tipo):
        status,historico  =self.API.get_position_history_v2(tipo,10,0,0,0)
        
        if(tipo =='digital-option'):
            for item in historico['positions']:
                print('Hora:',time_convert(item['close_time'] /1000), 'PAR:',str(item['raw_event']['instrument_underlying']) ,
                'Investimento:',str(item['invest']),
                'Direção:',str(item['raw_event']['instrument_dir']),
                'Resultado:', 'Loss' if  item['close_profit'] == 0 else 'Win' ,
                'Lucro:',round (item['close_profit'] - item['invest'],2)  if item['close_profit'] != 0 else item['invest'] * -1)
        else:

            for item in historico['positions']:
                print('Hora:',time_convert(item['close_time'] /1000), 'PAR:',str(item['raw_event']['currency']) ,
                'Investimento:',str(item['invest']),
                'Direção:',str(item['raw_event']['direction']),
                'Resultado:',  item['raw_event']['result'],
                'Lucro:',round (item['close_profit'] - item['invest'],2)  if item['close_profit'] != 0 else item['invest'] * -1)
        
        
        def Operacao_Binaria_Call(self,par,valor,tempoOperacao =1):
            # par ='EURUSD-OTC'
            # entrada =2
            direcao ='call'
            # tempoOperacao =1 # (1,5,15)

            status,id = self.API.buy(valor,par,direcao,tempoOperacao)

            if(status):
                print(self.API.check_win_v3(id))
                print('\n')
                
        
        def Operacao_Digital_Call(self,par,entrada,tempoOperacao =1):
            # par ='EURUSD-OTC'
            # entrada =2
            direcao ='call'
            # tempoOperacao =1 # (1,5,15)

            id = self.API.buy_digital_spot(entrada,par,direcao,tempoOperacao)

            if isinstance(id,int):
                while True:
                    status,lucro =API.check_win_digital_v2(id)
                    if(status):
                        if(lucro < 0):
                            print('resultado: Win', 'Ganho:',str(round(lucro,2)))
                        else:
                            print('resultado: Loss', 'Perca:',str(round(entrada,2))) 
                        break
            
        
        
        
    
       
        