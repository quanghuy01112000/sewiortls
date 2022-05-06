import requests
import json

url = "https://demo.sewio.net/sensmapserver/api/anchors"

headers = {
    "X-ApiKey": "171555a8fe71148a165392904",
}

response = requests.request("GET", url, headers=headers)
output=json.loads(response.text)
print(response.text)
print(output['results'])
array = output['results']
print(array[0])
anchor = array[0]
print(anchor['title'])
print()