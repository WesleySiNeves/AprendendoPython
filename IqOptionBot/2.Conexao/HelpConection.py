
import time
import pandas as pd
from datetime import datetime  
from datetime import timedelta 
import json



x = datetime(2021, 3, 23)
    
horarioOperacao = '2021-03-23 '+'00:20:57'
    
horaLimite = (datetime.strptime(horarioOperacao, '%YYYY-%MM-%DD %H:%M:%S') + timedelta(seconds=4))
 
print(horarioOperacao,horaLimite)

