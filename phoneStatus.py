#!/usr/bin/env python
import json
import http.client
USERNAME="pewdiepie" #replace with channel username

file = open('/home/manuwwa/.config/polybar/homeAssistant.json')
fileData = json.load(file)

conn = http.client.HTTPSConnection(""+fileData["homeAssistantUrl"])

payload = ""

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer "+fileData["token"]
    }

conn.request("GET", "/api/states/"+fileData["bateryLevelEntityId"], payload, headers)

res = conn.getresponse()
respCode = res.status
if respCode != 200:
    print("\uf3cd\uf056")
else:
    data = res.read()
    state = json.loads(data)["state"]

    conn.request("GET", "/api/states/"+fileData["batteryStatusEntityyId"], payload, headers)

    res = conn.getresponse()
    data = res.read()
    charging = json.loads(data)["state"]

    if charging == "charging":
        print("\uf3cd\uf0e7 {:,d}%".format(int(state)))
    else :
        print("\uf3cd {:,d}%".format(int(state)))    
