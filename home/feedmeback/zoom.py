import sys
import time
import requests
import authlib
import os
from datetime import date
import urllib.request
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional, Dict, Union, Any
from authlib.jose import jwt
from requests import Response
import http.client
import json
from ast import literal_eval

env_path = Path('.')/'tokens.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("ZOOM_API_KEY")
API_SECRET = os.getenv("ZOOM_API_SECRET")
ASSEMBLY_AI_TOKEN = os.getenv("ASSEMBLYAI_TOKEN")



class Zoom:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.jwt_token_exp = 518400
        self.jwt_token_algo = "HS256"

    def generate_jwt_token(self) -> bytes:
        iat = int(time.time())

        jwt_payload: Dict[str, Any] = {
            "aud": None,
            "iss": self.api_key,
            "exp": iat + self.jwt_token_exp,
            "iat": iat
        }

        header: Dict[str, str] = {"alg": self.jwt_token_algo}

        jwt_token: bytes = jwt.encode(header, jwt_payload, self.api_secret)

        return jwt_token


zoom = Zoom(API_KEY, API_SECRET)
jwt_token: bytes = zoom.generate_jwt_token()
jwt_token_str = jwt_token.decode('UTF-8')

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
files = []
for i in range(0,2):
    hayy = sayy[i]
    link = hayy["download_url"]
    date_ = hayy["recording_end"]
    dayz = date_[0:10]
    poom = date.today()
    files.append(link)

for link in files:
    authorized_url = link + "?access_token=" + "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlgyMzFFcjhfUW5xS3VxTmN6MHhETHciLCJleHAiOjE2NzI1Mjc1NDAsImlhdCI6MTY1NTQ3MzM0N30.0n8ph_QaekvRxcTUr0zZotD6_9FPVXqW65TtEIQQtOI"
    endpoint = 'https://api.assemblyai.com/v2/transcript'

    json = {
        'audio_url': authorized_url
    }

    heads = {
        'authorization': ASSEMBLY_AI_TOKEN,
        'content-type': 'application/json'
    }

    resp = requests.post(endpoint, json=json, headers=heads)
    status_point = 'https://api.assemblyai.com/v2/transcript/' + resp.json()['id']

    status_header = {'authorization':ASSEMBLY_AI_TOKEN} 

    status_check = requests.get(status_point, headers=status_header)

    while status_check.json()['status'] in ['queued', 'processing']:
        status_check = requests.get(status_point, headers=status_header)
        time.sleep(5)
        continue

  #  print(status_check.json()['status'])
    print('\n', status_check.json()['text'])
  #  print('\n', status_check.json())





    