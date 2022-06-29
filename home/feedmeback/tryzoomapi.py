from ast import literal_eval
from datetime import date
import json
import http.client
conn = http.client.HTTPSConnection("api.zoom.us")
headers = {
    'authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlgyMzFFcjhfUW5xS3VxTmN6MHhETHciLCJleHAiOjE2NzI1Mjc1NDAsImlhdCI6MTY1NTQ2MzAwMH0.Bs7RM38Tna6wcDJ9RVvHhGhGFaUjXhmZd_VKykfxNKo",
    'content-type': "application/json"
    }
conn.request("GET", "/v2/meetings/89954236062/recordings", headers=headers)
res = conn.getresponse()
data = res.read()
totry_json = data.decode("utf-8")
mooo = literal_eval(totry_json)
lop = json.dumps(mooo, indent=4, sort_keys=True)
dayy = json.loads(lop)
sayy = dayy["recording_files"]
files = {}
for i in range(len(sayy)):
    hayy = sayy[i]
    link = hayy["download_url"]
    date_ = hayy["recording_end"]
    dayz = date_[0:10]
    poom = date.today()
    print(link)
    print(dayz)
    print(poom)

#hayy = sayy[1]
#fetchy = json.loads(totry_json)
#show = json.dumps(fetchy, indent=4, sort_keys=True)
#print(hayy["download_url"])