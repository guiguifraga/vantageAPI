import json
from pathlib import Path
from os.path import exists
from datetime import datetime, timedelta
authTokenExpiresTime = ""
authTokenCreatedDatetime = ""
authToken = ""

def writeToken(file, data):
    tokenFile = open(file,"w")
    tokenFile.write(data)
    tokenFile.close()
    
def getToken():
    global authToken, authTokenExpiresTime, authTokenCreatedDatetime
    token = Path("token.dat").read_text()
    authToken = json.loads(token)["AuthenticationResult"]["IdToken"]
    authTokenExpiresTime = json.loads(token)["AuthenticationResult"]["ExpiresIn"]
    authTokenCreatedDatetime =  json.loads(token)["ResponseMetadata"]["HTTPHeaders"]["date"]
    
def validToken(tokenDT, tokenVAL): 
    tokenDateTime = datetime.strptime(tokenDT,'%a, %d %b %Y %H:%M:%S %Z')
    expireTokenDT = tokenDateTime + timedelta(seconds=tokenVAL)
    return True if datetime.now() < (expireTokenDT - timedelta(seconds=200)) else False

def fileExists(file):
    return exists(Path(file))

def createFile(file):
    tokenFile = Path(file)
    tokenFile.touch(exist_ok=True)

    
