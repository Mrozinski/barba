#!/usr/bin/python3.7
import pandas as pd
import numpy as np
import init.init as files
import scr.logs as logs
import scr.preProcessing as pre
import scr.readFile as rf

def main():
	logs.onStart()
	for fileName in files.files:
		df=rf.readFile(fileName)
		if len(df.index) == 0:
			print('error')
		else:
			print(fileName)
			print(df.head())
			print(pre.toSmallDf(df).head())
			#print(pre.toSmallDf2(df).head())
			#print(pre.toSmallDf3(df).head())
			#print(pre.toSmallDf3(df).head())
	logs.onExit()
	return 0

main()