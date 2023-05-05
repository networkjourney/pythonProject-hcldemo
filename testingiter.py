import requests

url = "https://172.16.24.80:443/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = ""
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
