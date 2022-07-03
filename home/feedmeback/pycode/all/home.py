from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, File, UploadFile, Request, APIRouter, Form
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
from core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Response, File, UploadFile, Form, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from boool import *
from book import *



templates = Jinja2Templates(directory="templates")
home_router = APIRouter()

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

#deta = Deta("a0hvh7kc_gzF99MiBbpsyD5v8fCusouRL91mcLYgd")
deta = Deta("a0k234l6_wDYfTpyYMBwzaCN7K39s8n564Ce2N9wm")
drive = deta.Drive("videos")

@home_router.get("/")
async def homepage(request:Request):
    return templates.TemplateResponse("pages/home.html", {"request":request})

@home_router.get("/userformatted")
async def otherfeedback(request:Request):
    return templates.TemplateResponse("pages/mmo.html", {"request":request})

@home_router.post("/userformatted")
async def otherfeedback(request:Request, feedbacktxt: str = Form(...), fullname: str = Form(...), email: str = Form(...), file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)

    kitchen = ["tastes", "tasted", "taste", "salt", "salty",  "spicy"  "too spicy", "hair in the food", "food", "dirty cutlery", "cutlery", "stale", "cutleries", " water to drink", "coffee", "cola", "cold food", "delay in food service", "vegetarian", "vegan", "meat", "sea food", "food quantity", "eat", "ate", "drink", "chilli", "breakfast", "lunch", "dinner", "snacks", "deserts", "cakes", "beer", "alcohol", "vodka", "whiskey", "halal", "fish", "rotten", "fruit", "fruits", "cook", "cooked", "salad", "fresh food", "vegetables", "refrigerated", "restaurant", "cocktail"]
    maintenance = ["plumbing", "electric fan", "air-conditioner", "water heater", "electric sockets", "docking station", "sockets", "drier", "light bulbs", "vending machine", "key", "elevator", "taps", "TV", "television is not coming on", "key card", "lockers", "hot water", "cold water", "windows", "shower", "lost keys", "stuck in the elevator", "heating", "room temperature", "fire alarm", "fire extinguisher", "extinguishers", "heater", "cupboards", "wardrobes", "the lift" ]
    house_keeping = ["hair in bathroom", "dirty room", "unclean floor", "dust", "dusty", "smelling rugs", "bed sheets", "bed spread", "patches on the walls", "unclean toilets", "dirty toilets", "dirty wash hand basin", "wastebins", "thrash under the bed", "litter", "littered", "clean", "mirrors", "toiletries", "toilet papers", "handwash", "soap, towels", "hand towels", "shampoo", "dirty bathtub", "toothbrush", "toothpastes", "hair brush", "floor mats", "wipes", "cobwebs", "bloodstains", "oil stains", "food crumbs all over", "pyjamas", "slippers", "needs cleaning", "needs to be washed", "needs to be cleaned", "is not clean", "are not clean", "mopped", "mop the floor"   ]
    poop = []
    for i in kitchen:
        if i in feedbacktxt:
            if "to_kitchen" in poop:
                break
            else:
                poop.append("to_kitchen")
        else:
            continue


    for i in maintenance:
        if i in feedbacktxt:
            if "to_maintenance" in poop:
                break
            else:
                poop.append("to_maintenance")
        else:
            continue                

    for i in house_keeping:
        if i in feedbacktxt:
            if "to_housekeeping" in poop:
                break
            else:
                poop.append("to_housekeeping")
        else:
            continue 
        
    if poop == []:
        poop.append("reception")        
    for i in poop:
        if i == "to_kitchen":
            blake = requests.post(
                url_moon,
                auth=("api", api_key),
                data={"from": origin__,
                    "to": "Emmanuel Olorunfemi <feedmeback.foodbeverage@gmail.com>",
                    "subject": "New Customer Feedback",
                    "text": f"{fullname} left a feedback: '{feedbacktxt}'. A short video was also uploaded, to access the video copy the following link into your web browser or click on it: http://127.0.0.1:8000/download/{res}. You can reach {fullname} back on this email address: {email}"})

        elif i == "to_maintenance":
            blake = requests.post(
                url_moon,
                auth=("api", api_key),
                data={"from": origin__,
                    "to": "Emmanuel Olorunfemi <feedmeback.maintenance@gmail.com>",
                    "subject": "New Customer Feedback",
                    "text": f"{fullname} left a feedback: '{feedbacktxt}'. A short video was also uploaded, to access the video copy the following link into your web browser or click on it: http://127.0.0.1:8000/download/{res}. You can reach {fullname} back on this email address: {email}"})

        elif i == "to_housekeeping":
            blake = requests.post(
                url_moon,
                auth=("api", api_key),
                data={"from": origin__,
                    "to": "Emmanuel Olorunfemi <feedmeback.housekeeping@gmail.com>",
                    "subject": "New Customer Feedback",
                    "text": f"{fullname} left a feedback: '{feedbacktxt}'. A short video was also uploaded, to access the video copy the following link into your web browser or click on it: http://127.0.0.1:8000/download/{res}. You can reach {fullname} back on this email address: {email}"})
        
        else:
            blake = requests.post(
                url_moon,
                auth=("api", api_key),
                data={"from": origin__,
                    "to": "Emmanuel Olorunfemi <feedmeback.reception@gmail.com>",
                    "subject": "New Customer Feedback",
                    "text": f"{fullname} left a feedback: '{feedbacktxt}'. A short video was also uploaded, to access the video copy the following link into your web browser or click on it: http://127.0.0.1:8000/download/{res}. You can reach {fullname} back on this email address: {email}"})



        status_msg = "Feedback successfully submitted"
        if res:
            if blake:
                return templates.TemplateResponse("pages/mmo.html", {"request":request, "msg": status_msg})
        else:
            raise HTTPException(status_code = 404, detail=  "Id not found")


@home_router.get("/login")
async def admin_login(request:Request):
    return templates.TemplateResponse("pages/login.html", {"request":request})

    
@home_router.post("/login/administrator")
async def admin_login(request:Request, username: str = Form(...), password: str = Form(...)):
    if username in authorized:
        if password == authorized.get(username):
            msgout = "Login was successful"
            ogre = get_transcript()
            transcript = ogre[0]
            link = ogre[1]

            base = Sorting_feedback(transcript, link).sort_now()
            if username == "kitchen_admin":    
                if "to_kitchen" in base:
                    msg_pack_one = transcript
                    msg_pack_two = link[0:32]
                    msg_pack_three = link[33:]
                else:
                    msg_pack_one = "No designated feedback at this time"
                    msg_pack_two = ""
                    
            elif username == "maintenance_admin":
                if "to_maintenance" in base:
                    msg_pack_one = transcript
                    msg_pack_two = link[0:32]
                    msg_pack_three = link[33:]
                else:
                    msg_pack_one = "No designated feedback at this time"
                    msg_pack_two = ""

            elif username == "housekeeping_admin":
                if "to_housekeeping" in base:
                    msg_pack_one = transcript
                    msg_pack_two = link[0:32]
                    msg_pack_three = link[33:]
                else:
                    msg_pack_one = "No designated feedback at this time"
                    msg_pack_two = ""
            elif username == "reception_admin" or username == "admin_overlord":
                    msg_pack_one = transcript
                    msg_pack_two = link[0:32]
                    msg_pack_three = link[33:]
            
            return templates.TemplateResponse("pages/landing.html", {"request":request, "msg": msgout, "username": username, "message_one": msg_pack_one, "message_two": msg_pack_two, "message_three":msg_pack_three})
        else:
            raise HTTPException(status_code=404, detail="Password incorrect, go back and try again with the right credentials or contact Head Administrator")
    else:
        raise HTTPException(status_code = 404, detail=  "Admin User login details provided were incorrect")



@home_router.get("/download/{name}")
def download_video(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="video/mp4")