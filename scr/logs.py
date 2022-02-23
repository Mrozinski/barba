from datetime import datetime 
from pathlib import Path


# Własny plik ninicjujący zmienne konfiguracyjne 
import init.init as files
import scr.rwFile as rw

# Zmienna logFile zapisuje informacje na temat miejsca przechowywania
# plików z logami (historią działania programu)
# jest składowe: 
# files.logDir - oznacza katalog docelowy, zadeklarowana w pliku init/init.py
# files.logFile - oznacza nazwę pliku, zadeklarowana w pliku init/init.py
logFile=files.logDir+files.logFile

# Zmienna reportFile zapisuje informacje na temat miejsca przechowywania
# plików z wynikami działań programu
# jest składowe: 
# files.logDir - oznacza katalog docelowy, zadeklarowana w pliku init/init.py
# files.readFileReport - oznacza nazwę pliku, zadeklarowana w pliku init/init.py

reportFile=files.reportDir+files.readFileReport

def writeToLogFile(msg):
	rw.dirCheck(files.logDir)
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg} \n')
	f.close()

def onStart(msg="launching the application"):
	rw.dirCheck(files.logDir)
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg} \n')
	f.close()

def onFileOpenError(fileName, msg="Error opening the file"):
	rw.dirCheck(files.logDir)
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg}: {fileName}\n')
	f.close()

def onExit(msg="Close the program"):
	rw.dirCheck(files.logDir)
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg}\n')
	f.close()

def onFileOpenSuccess(fileName, msg="Opening the file successful"):
		rw.dirCheck(files.logDir)
		f=open(logFile, "a")
		time=datetime.now()
		f.write(f'{time} {msg}: {fileName}\n')
		f.close()

def fileReadReport(filename, records=0, dTime=0, msg="file opening report:", msg2="records readed"):
	rw.dirCheck(files.reportDir)
	time=datetime.now().strftime(files.timeFormat)
	f=open(files.reportDir+filename+"_"+time,"a")
	f.write(f'{filename} {msg}\n')
	f.write(f'{records} {msg2}\n')
	f.write(f'Duration: {dTime} s\n')
	f.close()

def logTime(funName, time):
	writeToLogFile(f'{funName} duration {time} ')
