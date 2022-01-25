import pandas as pd
import time

import logs as logs

# Funkcja przyjmuje jako argument DataFrame
# wynikiem działania jest pełen numer oryginalny 
# oraz jego składowe jako oddzielne kolumny

def toSmallDf(df):
	start = time.time()
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	dfTemp['sex']=dfTemp.apply(lambda x: x.fullNumber[0], axis=1)
	dfTemp['country']=dfTemp.apply(lambda x: x.fullNumber[1:4], axis=1)
	dfTemp['id']=dfTemp.apply(lambda x: x.fullNumber[4:], axis=1)
	end = time.time()
	duration = end-start
	logs.logTime(__name__, duration)
	return dfTemp

# Funkcja pobiera numer osobnika posiadający 16 znaków 
# w rezultacie zwraca 3 wartości w foracie string:
# sex - 1 znak
# countryCode - 3 znaki 
# id - 12 znaków 

def splitID(fullNumber):
	sex = fullNumber[0]
	countryCode = fullNumber[1:4]
	id=fullNumber[4:]
	return sex, countryCode, id
