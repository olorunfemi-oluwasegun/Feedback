from zoom import *
import json
from book import *

class Sorting_feedback:
    def __init__(self, transcript, link):
        self.transcript = transcript
        self.link = link
        self.kitchen = ["tastes", "taste", "salt", "salty",  "spicy"  "too spicy", "hair in the food", "food", "dirty cutlery", "cutlery", "stale", "cutleries", " water to drink", "coffee", "cola", "cold food", "delay in food service", "vegetarian", "vegan", "meat", "sea food", "food quantity", "eat", "ate", "drink", "chilli", "breakfast", "lunch", "dinner", "snacks", "deserts", "cakes", "beer", "alcohol", "vodka", "whiskey", "halal", "fish", "rotten", "fruit", "fruits", "cook", "cooked", "salad", "fresh food", "vegetables", "refrigerated", "restaurant", "cocktail"]
        self.maintenance = ["plumbing", "electric fan", "air-conditioner", "water heater", "electric sockets", "docking station", "sockets", "drier", "light bulbs", "vending machine", "key", "elevator", "taps", "TV", "television is not coming on", "key card", "lockers", "hot water", "cold water", "windows", "shower", "lost keys", "stuck in the elevator", "heating", "room temperature", "fire alarm", "fire extinguisher", "extinguishers", "heater", "cupboards", "wardrobes", "the lift" ]
        self.house_keeping = ["hair in bathroom", "dirty room", "unclean floor", "dust", "dusty", "smelling rugs", "bed sheets", "bed spread", "patches on the walls", "unclean toilets", "dirty toilets", "dirty wash hand basin", "wastebins", "thrash under the bed", "litter", "littered", "clean", "mirrors", "toiletries", "toilet papers", "handwash", "soap, towels", "hand towels", "shampoo", "dirty bathtub", "toothbrush", "toothpastes", "hair brush", "floor mats", "wipes", "cobwebs", "bloodstains", "oil stains", "food crumbs all over", "pyjamas", "slippers", "needs cleaning", "needs to be washed", "needs to be cleaned", "is not clean", "are not clean", "mopped", "mop the floor"   ]


    def sort_now(self):
        poop = []
        for i in self.kitchen:
            if i in self.transcript:
                if "to_kitchen" in poop:
                    break
                else:
                    poop.append("to_kitchen")
            else:
                continue


        for i in self.maintenance:
            if i in self.transcript:
                if "to_maintenance" in poop:
                    break
                else:
                    poop.append("to_maintenance")
            else:
                continue                

        for i in self.house_keeping:
            if i in self.transcript:
                if "to_housekeeping" in poop:
                    break
                else:
                    poop.append("to_housekeeping")
            else:
                continue     
        
        return poop

    def sort_away(self):
        cart = self.sort_now()
        for i in cart:
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

            return blake
                


def get_transcript():
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


    cluster = []
    for link in files:
        authorized_url = link + "?access_token=" + "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlgyMzFFcjhfUW5xS3VxTmN6MHhETHciLCJleHAiOjE2NzI1Mjc1NDAsImlhdCI6MTY1NTQ3MzM0N30.0n8ph_QaekvRxcTUr0zZotD6_9FPVXqW65TtEIQQtOI"
        endpoint = 'https://api.assemblyai.com/v2/transcript'

        json_ = {
            'audio_url': authorized_url
        }

        heads = {
            'authorization': ASSEMBLY_AI_TOKEN,
            'content-type': 'application/json'
        }

        resp = requests.post(endpoint, json=json_, headers=heads)
        status_point = 'https://api.assemblyai.com/v2/transcript/' + resp.json()['id']

        status_header = {'authorization':ASSEMBLY_AI_TOKEN} 

        status_check = requests.get(status_point, headers=status_header)

        while status_check.json()['status'] in ['queued', 'processing']:
            status_check = requests.get(status_point, headers=status_header)
            time.sleep(5)
            continue
        
        if status_check.json()['text'] in cluster:
            continue
        else: 
            cluster.append(status_check.json()['text'])
            cluster.append(f"To watch this video, click here: {link}")

    return cluster            


