import pandas as pd
import numpy as np
import init.init as files
import scr.logs as logs

def readFile(fileName):
	df=pd.DataFrame()
	try:
		df= pd.read_csv(fileName, sep='\s+', header=None, encoding='utf8')
	except:
		print("Error")
		logs.onFileOpenError(fileName)
		return df
	else:
		logs.onFileOpenSuccess(fileName)
		return df

logs.onStart()

for fileName in files.files:
	df=readFile(fileName)
	if df.empty:
		print(fileName)
	else:
		print(fileName)
		print(df.head())

logs.onExit()
