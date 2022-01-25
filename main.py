import pandas as pd
import numpy as np
import init.init as files
import scr.logs as logs
import scr.preProcessing as pre
import scr.readFile as rf



def dupFullNumber(df):
	return(df[df.duplicated(subset=['fullNumber'])])

logs.onStart()

for fileName in files.files:
	df=rf.readFile(fileName)
	if df.empty:
		print(fileName)
	else:
		print(fileName)
		print(pre.toSmallDf(df).head())

logs.onExit()
