import Auth.utils
import Auth.auth_access
import handleLogs.handleLogs as Logs

def startAuth():
    if(Auth.utils.fileExists("token.dat")):
        Auth.utils.getToken()
        if(Auth.utils.validToken(Auth.utils.authTokenCreatedDatetime,Auth.utils.authTokenExpiresTime)):
            print('you are already authenticated')
            Logs.addLog('Success','Tried to authenticate but are already authenticated')
        else:
            Auth.auth_access.authCognito()
    else:
        Auth.utils.createFile("token.dat")
        Auth.auth_access.authCognito()

