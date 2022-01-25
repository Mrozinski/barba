import pandas as pd
import time
import scr.logs as logs

def readFile(fileName):
	start = time.time()
	df=pd.DataFrame()
	try:
		df= pd.read_csv(fileName, sep='\s+', header=None, encoding='utf8')
		end = time.time()
		duration=round(end-start,2)
	except:
		print("Error")
		logs.onFileOpenError(fileName)
		return df, start
	else:
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadReport(fileName, records=df.shape[0], acTime=start, dTime=duration)
		return df, start
