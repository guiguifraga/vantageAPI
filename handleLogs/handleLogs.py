
from datetime import datetime

def addLog(msgType, msg):

    logFile = r".\log.dat"
    log = open(logFile,"a")
    appended_msg = "\nType:{2} - {0}: _msg_ {1}".format(str(datetime.now()),msg,msgType) 
    log.write(appended_msg)
    log.close
