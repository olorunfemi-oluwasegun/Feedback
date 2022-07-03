from fastapi import FastAPI, File, UploadFile, Request, APIRouter
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import smtplib
from credentials import *
from email.message import EmailMessage
import requests
from email.mime.text import MIMEText
from ast import literal_eval
from datetime import date
import json
import http.client
from fastapi.templating import Jinja2Templates
from pycode.all.home import home_router
from core.config import settings
from fastapi.staticfiles import StaticFiles



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

#app = FastAPI()
deta = Deta("a0k234l6_wDYfTpyYMBwzaCN7K39s8n564Ce2N9wm")
drive = deta.Drive("videos")

def include_path(app):
    app.include_router(home_router)

#def configure_static(app):
  #  app.mount("/statik", StaticFiles(directory="statik"), name="statik")
  #fllfllfllfflllfllfllfflfllfllfllfffllfffllllflfll

def start_up():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_path(app)
    #configure_static(app)
    return(app)

app = start_up() 



#@app.get("/aaa", response_class=HTMLResponse)
#def render():
#    return """
#    <form action="/upload" enctype="multipart/form-data" method="post">
#        <input name="file" type="file">
#        <input type="submit">
#    </form>
   

#    """

"""
@app.post("/upload")
def upload_video(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)

    

    msg = MIMEText(f"To access the feedback received copy the following link into your web browser or click on it: http://feedmeback.deta.dev/download/{res}")
    msg['Subject'] = "New Customer Feedback"
    msg['From']    = "postmaster@sandbox5caa73bd91e34c2297c29292a8abd706.mailgun.org"
    msg['To']      = "olorunfemisegun1994@gmail.com"

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandbox5caa73bd91e34c2297c29292a8abd706.mailgun.org', '9769963bae3ecc3d13cfd0e419f74015-523596d9-fb888878')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    return "Feedback submitted sucessfully."

@app.get("/download/{name}")
def download_video(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="video/mp4")

@app.get("/dowload_video")
async def save_token(request:Request):
    sayy = dayy["recording_files"]
    files = []
    for i in range(0,2):
        hayy = sayy[i]
        link = hayy["download_url"]
        date_ = hayy["recording_end"]
        dayz = date_[0:10]
        poom = date.today()
        files.append((date_ , link))
    return files


@app.get("/play_video")
async def save_token(token:str):
    with open('tokens.txt', 'w') as access:
        access.write(token)
    return "Token Generated on Server"
"""