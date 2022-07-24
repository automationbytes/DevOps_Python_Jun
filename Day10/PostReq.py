import requests
import json
import jsonpath
from jsonpath_ng import jsonpath, parse

myobj = {
        "City": "Chennai",
        "Country": "India",
        "Name": "Tammy"
}
req = requests.post("http://webservice.toscacloud.com/rest/api/Shops_V2/",json = myobj )
print(req.status_code)
print(json.dumps(req.json(),indent=4))
