from flask import Flask
app = Flask(__name__)
import requests
from requests.auth import HTTPBasicAuth
import json

@app.route("/createJIRA", methods=['POST'])
def createJIRA():

    url = "enter-jira-url/rest/api/3/project"

    API_TOKEN="enter apt token of jira"
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