from datetime import datetime 
import init.init as files

logFile=files.logDir+files.logFile
reportFile=files.logDir+files.readFileReport

def onStart(msg="launching the application"):
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg} \n')
	f.close()

def onFileOpenError(fileName, msg="Error opening the file"):
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg}: {fileName}\n')
	f.close()

def onExit(msg="Close the program"):
	f=open(logFile, "a")
	time=datetime.now()
	f.write(f'{time} {msg}\n')
	f.close()

def onFileOpenSuccess(fileName, msg="Opening the file successful"):
        f=open(logFile, "a")
        time=datetime.now()
        f.write(f'{time} {msg}: {fileName}\n')
        f.close()

def fileReadRaport(filename, records=0, msg="file opening report:", msg2="records readed"):
	time=datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
	f=open(reportFile+time,"w")
	f.write(f'{filename} {msg}\n')
	f.write(f'{records} {msg2}\n')
	f.close()
