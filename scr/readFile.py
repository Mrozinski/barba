import pandas as pd
import numpy as np
import time
import scr.logs as logs
from dask import dataframe as ddf

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
		return df
	else:
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadReport(file_name(fileName)+'pandas', records=df.shape[0].compute(), dTime=duration)
		return df

def file_name(fileName):
	return fileName[fileName.rindex("/")+1:]

def readFile2(fileName):
	start = time.time()
	df=pd.DataFrame()
	try:
		array = np.loadtxt(fileName, dtype='str')
		df= pd.DataFrame(array)
		end = time.time()
		duration=round(end-start,2)
	except:
		print("Error")
		logs.onFileOpenError(fileName)
		return df
	else:
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadReport(file_name(fileName), records=df.shape[0], dTime=duration)
		return df

def readFile3(fileName):
	start = time.time()
	#df=dd.DataFrame()
	print(fileName)
	try:
		df= ddf.read_csv(fileName)
		end = time.time()
		duration=round(end-start,2)
	except:
		print("Error")
		logs.onFileOpenError(fileName)
		return df
	else:
		logs.onFileOpenSuccess(fileName); 
		logs.fileReadReport(file_name(fileName)+'dask', records=df.shape[0].compute(), dTime=duration)
		return df