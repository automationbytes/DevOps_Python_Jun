import requests
import json
import jsonpath
from jsonpath_ng import jsonpath, parse

req = requests.get("http://webservice.toscacloud.com/rest/api/Shops_V2/")
print(req.status_code)
#print(req.text)
#print(req.json())
print(json.dumps(req.json(),indent=4))
# for record in req.json():
#     if record['Id'] == 710:
#         record['Name'] = "Burra"
# json_data = json.loads(req.text)
# jsonpath_expr= parse('$.Name')
# first_name = jsonpath_expr.find(json_data)
# print("The First Name of the employee is: ", first_name[1].value)
#
#
