#!/usr/bin/python3.7
import pandas as pd
import numpy as np
import init.init as files
import scr.logs as logs
import scr.preProcessing as pre
import scr.readFile as rf
import scr.analytics as an

def main():
	dfList=[]
	logs.onStart()
	for fileName in files.files:
		df=rf.readFile(fileName)
		if len(df.index) == 0:
			print('error')
		else:
			print(fileName)
			#print(df.head())
			df =pre.toSmallDf(df)
			dfList.append(df)
			print(an.checkForDups(df))
	logs.onExit()
	return 0

main()