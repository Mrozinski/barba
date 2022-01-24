from datetime import datetime 
import init.init as files
logFile=files.logDir+"logs.log"

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

