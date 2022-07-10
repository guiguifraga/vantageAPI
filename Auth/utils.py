import json
from pathlib import Path
from datetime import datetime, timedelta
authTokenExpiresTime = ""
authTokenCreatedDatetime = ""
authToken = ""

def writeToken(token):
    tokenFile = open("token.dat","w")
    tokenFile.write(token)
    tokenFile.close()
    
def getToken():
    global authToken, authTokenExpiresTime, authTokenCreatedDatetime
    token = Path("token.dat").read_text()
    authToken = json.loads(token)["AuthenticationResult"]["AccessToken"]
    authTokenExpiresTime = json.loads(token)["AuthenticationResult"]["ExpiresIn"]
    authTokenCreatedDatetime =  json.loads(token)["ResponseMetadata"]["HTTPHeaders"]["date"]
    
def validToken(tokenDT, tokenVAL): 
    tokenDateTime = datetime.strptime(tokenDT,'%a, %d %b %Y %H:%M:%S %Z')
    expireTokenDT = tokenDateTime + timedelta(seconds=tokenVAL)
    return True if datetime.now() < (expireTokenDT - timedelta(seconds=200)) else False

print("teste")