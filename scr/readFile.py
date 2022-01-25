import pandas as pd
import time
import scr.logs as logs

def readFile(fileName):
	start = time.time()
	df=pd.DataFrame()
	try:
		df= pd.read_csv(fileName, sep='\s+', header=None, encoding='utf8')
		end = time.time()
		duration=end-start
	except:
		print("Error")
		logs.onFileOpenError(fileName)
		return df
	else:
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadReport(fileName, records=df.shape[0], dTime=duration)
		return df
