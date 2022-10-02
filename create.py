# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request
# FLASK = = = = = = = = = = = 

# CRED = = = = = = = = = = =
import googleapiclient.discovery
from google.oauth2 import service_account as google_oauth2_service_account
# CRED = = = = = = = = = = =

# QUICKSTART = = = = = = = = = = =
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# QUICKSTART = = = = = = = = = = =

# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/authentication')

def authentication():
    creds = google_oauth2_service_account.Credentials.from_service_account_info(
    {
  "type": "service_account",
  "project_id": "my-project-90818-learn-hun",
  "private_key_id": "5af4d0f2630d0c5701bbd094a4245c4d336396a7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDk76CnM/T/6sGI\n0S1UaK/mE0mSiVeZIY+KKsCn01mrdcVttTcyJPkgy8bBv9idWITlQbRGaAOgLudy\nTVbqHb0ma99koIBf2HI67z6fzMPJOw4q1VqG550Bj933v/GON8exdM2zr9HvaLXJ\nmTCloOwbV91O0O57X1uVBVz9oAZCLrJhPaHRKq2zr7asH5VgyX3eX772d1MCA3pS\ntyXbMVMXDdKji06FjV2ctRUVszr2zE2lcqtV4GVXlrUAKy9IOBbdRGkeVBW82qXz\nNCRXXkuLsRjd7JLawhHsKgpjAJLQBTKkvgfWggYtSV4VynsEDG8a3321SGphTgI0\ns4lgiiGpAgMBAAECggEAAuH+lqRpmSBiY//oT3gLAP1sr37xvrCkv1Nm/iYD6swO\nmqFNyuCaz34paE6rYl3XPJDNfZZ5Nzbn/LE7HzMVKurwUvLPcwWFeLcDBZ2dOIc5\nGDJ8E5dOi5K9c41z8/vBVLt5DKJx5Q8fPOTkLy2902FRnNi2LBEJFPEOmPX/Ji2s\nwQD9qhRmEDMOQBiEWTTE0gPoISYp062QcIc30SHItdNdo0iNuz3SK1yq7Fq2vDMS\nUYK0YuSTmxu2NGw5kSFY9mKCbRwCDnTvc74PLvmqIxm0DTkiySNVCx1lAs5h3Gaz\n2Qw4osX3CIotoKAaMf6FuFgR/f+elF0uBZ+JCt1HNQKBgQD7D1/NwUFOuB0N6pq3\n+NNy0seqZmpibBr5Pjerzqf9ZrBk6VCR2VA/cjmzk28npd0bzaTZZ709ncbpidXG\n1+Yfy6y4j24pSULKcXHeS6up0OZzaJgyghbhOQ0RE5d/NhvS2quSXM/YaIaVzQdN\nBdh1ZZNKrmtwe5Cd2JWmFWwUTQKBgQDpcM+9PWpLy/8Xw4esjnfbfsQpo7xK+7DJ\nBRf+FuWrvOejWOtlfXVe8WBhvBPPaEKOzXt91VUFi6WqErNnjZV7/6/KHRJjHg46\n/wCSMPhQ/jvnKvnymj3JB1qqnCSLy/2dmTFYZR0HOUGbIdZkBFb2ajbsWvkGnwJf\nEeGn62VgzQKBgQDJd2Hq7A0rTWXLWBtGTL/p4almXX87cgMHRd1I2rJGD9S3dd84\n2wmhkFkreMF3MIvJlvGVoMDkpCsOF5TcVz6M/1WgWUEOkoKtj/HPcCvWPxPfQuz3\ngxs3KyAINw+YfuQ/BUkvT5le0SpHJduY/HriYlubT3JaNl4rvLUCLSio9QKBgQCj\nM8Vorhk0aKgs+vxNfUT6ZYPLALfRTGlqAG+nqmZjTKw9HRtlVvLJr8MMUSsgY+m0\nYKAndw/70oe9gVl/2hJaIIXLrct/FDIquMCzdB0Gstc6ZGdeXss3Ujbm9EbwnWrv\n1XwUKozC0hq11FBImGgb2mIPmAJlyKElyiCS/xVfOQKBgH+Djwz8TPUIibKIK/cZ\nLgQWi7OmU5q7waRlYFEXa86qx1XhfNZI0hdDKQGFm6/E7xvlYfsvaxy3mWt2H7aP\nT395BTGaOvd1iMJc+KKG7/0dwsF9TNe2bLayukYn1pv/sax/CDMe9nWAWz47LyuH\ni5DwBThM9ioEUpec0sYCjl8B\n-----END PRIVATE KEY-----\n",
  "client_email": "appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com",
  "client_id": "115405775326578876255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/appointment-scheduler%40my-project-90818-learn-hun.iam.gserviceaccount.com"
    },
    scopes=['https://www.googleapis.com/auth/calendar'],
    subject='appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com'
    )
    return creds

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    #text = "webhook flask text response"
    #text = main()
    text_param =  main()
    text = text_param['text']
    event_id = text_param['event_id']

    res = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            text
                        ]
                    }
                }
            ]
        },
        "session_info": {
            "session" : "session_name",
            "parameters": {
                "event_id" : event_id
            }
        }
    }

    return res


def main():

    req = request.get_json(force=True)
    print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')

    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')

    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    print("DATE TIME PARAMETER:", year, month, day, hours, minutes, "summary: ", summary, "location: ",  location)
    #DATE TIME PARAMETERS: 2022.0 9.0 24.0 17.0 0.0

    sep = ","
    dt_parameter = str(int(year)) + sep + str(int(month)) + sep + str(int(day)) + sep + str(int(hours)) + sep + str(int(minutes))
    print('DATE TIME PARAMETERS: ',dt_parameter)

    #dt = datetime(2022, 09, 10, 01, 48, 34, 01)
    dt_str_date = datetime.datetime.strptime(dt_parameter, '%Y,%m,%d,%H,%M')
    #2022-09-25 00:00:00

    creds = authentication()
    service = build("calendar", "v3", credentials=creds)

    d = datetime.datetime.now().date()
    today = datetime.datetime(d.year, d.month, d.day, 10)+datetime.timedelta(hours=1)
    #2022-09-25 11:00:00
    #start = today.isoformat("T", "seconds")

    #start_parameter = datetime.datetime(2022, 9, 25, 12, 30, 0)

    start_parameter = dt_str_date

    start = start_parameter.isoformat("T", "seconds")

    #end = (today + datetime.timedelta(hours=1)).isoformat("T", "seconds")
    end = (start_parameter + datetime.timedelta(hours=1)).isoformat("T", "seconds")

    #event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',sendUpdates='all',
    event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',
       body={
           "summary": summary,
           "location": location,
           "description": "This is the description (parkolo/targyalo, stb)",
           "start": {"dateTime": start, "timeZone": "Europe/Budapest"},
           "end": {"dateTime": end, "timeZone": "Europe/Budapest"},
           "recurrence": {
                "RRULE": "FREQ=DAILY;COUNT=2"
            },
            "attendees": {
                "email": "tsystems.ai@gmail.com",
                "email": "sbrin@example.com",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 24 * 60},
                    {"method": "popup", "minutes": 10},
                ],
            },
            "colorId": 6,
       }
    ).execute()

    text = "Event created. Starts:" + event_result['start']['dateTime'] + " Ends: " + event_result['end']['dateTime'] + " id: " + event_result['id']

    text_param = {}
    text_param['text'] = text
    text_param['event_id'] = event_result['id']
  
    #return text
    return text_param

    app.run()