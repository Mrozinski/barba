import pandas as pd
import init.init as files
import scr.logs as logs

print(files.files)
try:
	df1= pd.read_csv(files.files[0])
except:
	print("Error")
else:
	logs.onStart()

print(df1.head())
