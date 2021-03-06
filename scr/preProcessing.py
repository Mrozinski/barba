from numpy import outer
import pandas as pd
import time

import scr.logs as logs

# Funkcja przyjmuje jako argument DataFrame
# wynikiem działania jest pełen numer oryginalny 
# oraz jego składowe jako oddzielne kolumny

def merge3DataFrame(df1, df2, df3, col):
	return df1.merge(df2, on=col, how='outer').merge(df3, on=col, how='outer')
	
def merge2DataFrame(df1, df2, col):
	return df1.merge(df2, on=col, how='outer')

def toSmallDf(df):
	start = time.time()
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	dfTemp['sex']=dfTemp.apply(lambda x: x.fullNumber[0], axis=1)
	dfTemp['country']=dfTemp.apply(lambda x: x.fullNumber[1:4], axis=1)
	dfTemp['id']=dfTemp.apply(lambda x: x.fullNumber[4:], axis=1)
	end = time.time()
	duration = end-start
	logs.logTime(toSmallDf.__name__, duration)
	return dfTemp

def toSmallDf2(df):
	start = time.time()
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	for index, row in dfTemp.iterrows():
		row["sex"]=row["fullNumber"][0]
		row["country"]=row["fullNumber"][1:4]
		row["id"]=row["fullNumber"][4:]
	end = time.time()
	duration = end-start
	logs.logTime(toSmallDf2.__name__, duration)
	return dfTemp

def toSmallDf3(df):
	start = time.time()
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	for line, row in enumerate(dfTemp.itertuples(),0):
		dfTemp.at[line,'sex']=row.fullNumber[0]
		dfTemp.at[line,'country']=row.fullNumber[1:4]
		dfTemp.at[line,'id']=row.fullNumber[4:]
	end = time.time()
	duration = end-start
	logs.logTime(toSmallDf3.__name__, duration)
	return dfTemp

def toSmallDf4(df):
	start = time.time()
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	for row in df.values:
		row["sex"]=row["fullNumber"][0]
		row["country"]=row["fullNumber"][1:4]
		row["id"]=row["fullNumber"][4:]
	end = time.time()
	duration = end-start
	logs.logTime(toSmallDf4.__name__, duration)
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
