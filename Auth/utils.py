import json
from pathlib import Path
authTokenExpiresTime = ""
authTokenCreatedDatetime = ""
authToken = ""

def writeToken(token):
    tokenFile = open("token.dat","w")
    tokenFile.write(token)
    tokenFile.close()
    


def checkToken():
    global authToken, authTokenExpiresTime, authTokenCreatedDatetime
    token = Path("token.dat").read_text()
    authToken = json.loads(token)["AuthenticationResult"]["AccessToken"]
    authTokenExpiresTime = json.loads(token)["AuthenticationResult"]["ExpiresIn"]
    authTokenCreatedDatetime =  json.loads(token)["ResponseMetadata"]["HTTPHeaders"]["date"]
    
