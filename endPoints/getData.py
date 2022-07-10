import requests
import json
from pathlib import Path
import Auth.utils

endPointsFile = open(Path("endPoints/endpoints.json"))
endPoints = json.load(endPointsFile)

def getData():
    Auth.utils.getToken()
    headers = {
        "authorization": Auth.utils.authToken
    }
    params = endPoints["apis"][0]["params"]
    response = requests.get(endPoints["apis"][0]["url"],params=params,headers=headers)
    print(response.json())



