import requests
import json
from pathlib import Path
import Auth.utils
import json
endPointsFile = open(Path("endPoints/endpoints.json"))
endPoints = json.load(endPointsFile)

def getData():

    print(range(len(endPoints["apis"])))
    for i in range(len(endPoints["apis"])):
        
        Auth.utils.getToken()
        headers = {
            "authorization": Auth.utils.authToken
        }
        params = endPoints["apis"][i]["params"]
        response = requests.get(endPoints["apis"][i]["url"],params=params,headers=headers)
        Auth.utils.createFile(Path(endPoints["apis"][i]["exportLocation"]))
        Auth.utils.writeToken(endPoints["apis"][i]["exportLocation"],json.dumps(response.json()))



