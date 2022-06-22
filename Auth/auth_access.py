import Auth.SETUP as SETUP
import Auth.utils as utils
import json
import boto3
from handleLogs.handleLogs import addLog

def authCognito():
    addLog("Start", "AWS Token service started")
    provider_client = boto3.client('cognito-idp', region_name=SETUP.region_name)
    try:
        addLog("Process", "Trying to get token")
        resp = provider_client.initiate_auth(AuthFlow=SETUP.AuthFlow, AuthParameters=SETUP.auth_data, ClientId=SETUP.client_id)
    except provider_client.exceptions.NotAuthorizedException as e:
        print("Erro de Auth:{}".format(e))
        addLog("Error",e)
    else:
        utils.writeToken(json.dumps(resp))
        addLog("Success", "Token Criado") 
    finally:
        addLog("Final", "AWS Token proccess was closed")

