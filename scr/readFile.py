import pandas as pd
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
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadRaport(fileName, records=df.shape[0])
		return df
