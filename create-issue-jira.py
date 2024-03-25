import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://moreaniket620.atlassian.net//rest/api/3/issue"
API_TOKEN="ATATT3xFfGF0MuX3YNTSZU8GGkp4do5sj6lXEIsOuCFzhJCBEsbJP0MgB9wYV-9lNnGg1FyowriYB7onSf6Qui94pH2IppAcPc547tyi2mCgs1iXIr_IGjDseMLpxLBTCd8w-sSNDAZ9CQdTAnmRbI_Xkph9WrLM8LnszrzUEevJZ_v2gxHQ99Y=ECE2BE2C"
auth = HTTPBasicAuth("moreaniket620@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First Jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "key": "KAN"
    },
    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))