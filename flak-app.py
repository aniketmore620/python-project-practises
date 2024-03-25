from flask import Flask
app = Flask(__name__)
import requests
from requests.auth import HTTPBasicAuth
import json

@app.route("/createJIRA", methods=['POST'])
def createJIRA():

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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0')