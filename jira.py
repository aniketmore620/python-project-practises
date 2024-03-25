# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://moreaniket620.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0MuX3YNTSZU8GGkp4do5sj6lXEIsOuCFzhJCBEsbJP0MgB9wYV-9lNnGg1FyowriYB7onSf6Qui94pH2IppAcPc547tyi2mCgs1iXIr_IGjDseMLpxLBTCd8w-sSNDAZ9CQdTAnmRbI_Xkph9WrLM8LnszrzUEevJZ_v2gxHQ99Y=ECE2BE2C"
auth = HTTPBasicAuth("moreaniket620@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[0] ["name"]
print(name)