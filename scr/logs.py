from datetime import datetime 
def onStart(msg="launching the application"):
	f=open("./log/logs.log", "a")
	time=datetime.now()
	f.write(f'{time} {msg} \n')
	f.close()
