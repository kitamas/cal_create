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

import locale

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
  "private_key_id": "cf8bd4105633c3cac528d1c8c4c66cc3b825e837",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeQrDkS5Rq/khX\nNoU01bLEbZHj/JjzwlcozMB0uRP+H9NYJytYrl4+vqhi3+EApY+bKpU/iB/A9tPC\nVIYjhXeACCXtNq6sz8hQDN6y+cKW5K4i2yd1xpeIlAXjo4M/uRIarlffgEi3MOAX\nRtTDskXvECuu2rXsIbgQEBzpCwJQhaVWnOHk4ONTJnEKSjvtuHXRZUc6GrabLrLU\nb4h1nDYh8+IVoUxpcZg0sW9XWpXw2O3kh8o6ADy4aH2KB9Sv4yktLLNcVWrqisei\nekA93NnWji5pG2DKuqjrmaZGA9SwOA5gT34EfrbL8zVFaEGgV7yp5ytrTg5vmtaw\nP36j58iJAgMBAAECggEAG5iV900NjYWXECwX2LFtuW5AuwBEHHc2Ew12/rN6Hr0m\ncW/tEUrgcLD2tD0FI0N7UcuAWGJwZQm1PaTW+hEvGAJzuJQpK8WUkI7Z81v1WDH6\ngmX0EMenC0ACceIEhCNNmpztgjHAnD73yF9HwPMQWkIX1+bXw5vSmGxy2hkbF3ac\nKehAlVB584QC8L191WtWPpx27pdNy2ncnlW6Xaail8NtGlCELLGrmicQUjgxZhsU\ngEZh/ZrTYm4ion5mWCYtbSvuXN++9Zy6kIdpYiFOroQuEr48L6l0KLmVvNsuZ1D0\nk4xdXJxtx0kacGr0tyg1VV3vut14vcSlDqbeDUy7DQKBgQC/5LuQVTJT3FiJ13sb\nCyJIuFVQAX2p1+TXsiKJh9Copaua0tvXygJtbGFEVmYKS3VwiC8OyESQQhATFORE\nYZYpek0UwhNggekg+asiMMSnPc/hHkxQdsxmT34sfmuooSeDvqrVPw6BW3i7Hb6Q\nB7lfydH+v6VejPKWm2q7sm6UpQKBgQDTIZJ/rdgknqnIENgcHwRJoKS3j2RcCvnK\nu0pXoumA9xq1/JFOCuGmRnscyga0d17fYGpER3iR5NL2YAksMSUEDyj+yFupHyfS\nTZzVVaeYNW3OKjDXwUDGYh2D3JkF7P6zeC9LLBkvwuhllvwC1URewWARBpreVGpH\nuZGRo6CLFQKBgHnO9yTif+TtzSIKr3F2OtgQcs8rcxpaGkC1KelFVjWHnIvV54lu\nCOZu0rtvYKyOQ8kgGUb351XvKYcDTvb9PzWrFbzkiSpMrLCq62/zpxFGUmvjMKwv\nDQaw1TXnNe3ABnZBlO1yboG8j8GvWuTQkmJ0mSFtg8qmC+OAWls1I66lAoGAZCvL\njBR5Nnao6ylCv6Tfrecv/39jCGCUv2E5FndO/kc/PxUEA9kZ0oAiLTiVEc6JDsZ5\n5MdcJyxAA3DxKSxv+YsP0kJRat5DUH5OaNFo4MiIvoY6AkPIbddjVYq2d59IAPKG\nzc2wbX62MG0ASH/THnn1EF7n35CBlGIw9L6DjzkCgYEAu0LhdTHuuM6DOAfh4ohw\n0oj2770Dyw0vQImp+4qbdocLqXIVOZYEIywGfi+OLuSxrSYsw2BuTAPAtIEmkuHx\n4cvV/XxcWWPY30B4Z2irOBIsIXJjfAO/DyCyDaX7Cmoy+NgoCwRSRzDeOiQ7ysw8\nhwrS/OoTx3BhHYJt+NO6qIM=\n-----END PRIVATE KEY-----\n",
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
    # check_open_text = check_open()
    # print("check_open_text",check_open_text)

    checked_start_text_o = check_open()

    starto = checked_start_text_o[0]
    endo = checked_start_text_o[1]
    summary = checked_start_text_o[2]
    location = checked_start_text_o[3]
    boolean = checked_start_text_o[5]


    print("webhook start start = starto ",checked_start_text_o[0])
    print("webhook end end  =",checked_start_text_o[1])
    print("summary  =",checked_start_text_o[2])
    print("location = ",checked_start_text_o[3])
    print("boolean = ",checked_start_text_o[5])

    text_param =  main(starto,endo,summary,location)

    text = text_param['text'] + checked_start_text_o[4] + "B= " + str(checked_start_text_o[5])
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


def main(starto,endo,summary,location):
    """
    req = request.get_json(force=True)
    # print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')

    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')

    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    # print("DATE TIME PARAMETERS:", year, month, day, hours, minutes, "summary: ", summary, "location: ",  location)
    # DATE TIME PARAMETERS: 2022.0 10.0 9.0 12.0 0.0 summary:  q location:  q

    dt_p_string = str(int(year)) + "," + str(int(month)) + "," + str(int(day)) + "," + str(int(hours)) + "," + str(int(minutes))
    # DATE TIME PARAMETERS STRING:  2022,10,9,12,0

    dt_p_obj = datetime.datetime.strptime(dt_p_string, '%Y,%m,%d,%H,%M')
    # 2022-09-25 00:00:00 - string to datetime object

    # start = dt_p_obj.isoformat("T", "seconds")
    """
    print("MAIN starto = ",starto)

    start = starto
    # 2022-10-09T12:00:00

    #end = (dt_p_obj + datetime.timedelta(hours=1)).isoformat("T", "seconds")
    end = endo

    creds = authentication()
    service = build("calendar", "v3", credentials=creds)

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

    # text = "Event created. Starts: " + event_result['start']['dateTime'] + " Ends: " + event_result['end']['dateTime'] + " id: " + event_result['id']

    # print(event_result['start']['dateTime']) 2022-10-10T15:00:00+02:00

    start_event = datetime.datetime.strptime(event_result['start']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')
    end_event = datetime.datetime.strptime(event_result['end']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')

    text = "Kezdő időpont: " + start_event.strftime("%B %A %H:%M") + " Vége: " + end_event.strftime("%B %A %H:%M")

    text_param = {}
    text_param['text'] = text
    text_param['event_id'] = event_result['id']
  
    #return text
    return text_param

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    # return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + datetime.timedelta(hours=t.minute // 30))

    # Rounds to next hour by adding a timedelta hour + 1
    if t.minute != 0:
        return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour + 1))
    else:
        return (t.replace(second=0, microsecond=0, minute=0))

def check_open():
    current_dateTime = datetime.datetime.now() + datetime.timedelta(hours=2)
    current_dateTime_rounded = hour_rounder(current_dateTime)

    current_hour_rounded = current_dateTime_rounded.strftime('%H:%M')
    print("CURRENT HOUR ROUNDED:", current_hour_rounded)

    req = request.get_json(force=True)
    # print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')

    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')

    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    open_start_time = ["12:00", "12:00", "12:00", "08:00", "08:00", "08:00", "12:00"]
    open_end_time = ["19:00", "19:00", "19:00", "19:00", "17:00", "13:00", "15:00"]

    weekDays = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")

    dt_p_string = str(int(year)) + "," + str(int(month)) + "," + str(int(day)) + "," + str(int(hours)) + "," + str(int(minutes))
    # DATE TIME PARAMETERS STRING:  2022,10,9,12,0

    dt_p_obj = datetime.datetime.strptime(dt_p_string, '%Y,%m,%d,%H,%M')
    # 2022-09-25 00:00:00 - string to datetime object

    dt_p_week_day = dt_p_obj.weekday()
    dt_p_week_day_name = weekDays[dt_p_week_day]
    print("dt_p_week_day_name:", dt_p_week_day_name)

    dt_p_obj_rounded = hour_rounder(dt_p_obj)

    hour_rounded = dt_p_obj_rounded.strftime('%H')
    print("PARAM HOUR ROUNDED:", hour_rounded)

    start = dt_p_obj.isoformat("T", "seconds")
    print("START from parameter = ",start,type(start))
    # START from parameter =  2022-10-15T17:00:00 <class 'str'>

    end = (dt_p_obj + datetime.timedelta(hours=1)).isoformat("T", "seconds")

    duration = 1

    if current_dateTime > dt_p_obj:
        print("A jelenlegi idő: ",current_dateTime," ",dt_p_obj,"már elmúlt. Adjon meg másik időpontot.")
        #check_open_text = "A jelenlegi idő: " + current_dateTime + " " + dt_p_obj + "már elmúlt. Adjon meg másik időpontot."
        check_open_text = "A megadott idő már elmúlt. Adjon meg másik időpontot."
        check_open_boole = False

        checked_start = [start,end,summary,location,check_open_text,check_open_boole] 
        return checked_start

    #locale.setlocale(locale.LC_ALL, "HU_hu.utf8")
    #locale.setlocale(locale.LC_TIME, "HU_hu.utf8")
    #print("LOCALE LOCALE",current_dateTime.strftime('%A, %a, %B, %b'))

    print("open_start_time:", open_start_time[dt_p_week_day])
    print("open_end_time:", open_end_time[dt_p_week_day])

    if hour_rounded < open_start_time[dt_p_week_day]:
        print("KORÁN", hour_rounded, "<", open_start_time[dt_p_week_day])
        check_open_text = " KORÁN. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        #check_open_text = " KORÁN. " 
        check_open_boole = False

    if hour_rounded >= open_end_time[dt_p_week_day]:
        #print("KÉSŐN", hour_rounded - duration, ">=", open_end_time[dt_p_week_day])
        print("KÉSŐN", hour_rounded, ">=", open_end_time[dt_p_week_day])
        check_open_text = " KÉSŐN. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        #check_open_text = " KÉSŐN. " 
        check_open_boole = False

    if hour_rounded >= open_start_time[dt_p_week_day] and hour_rounded <= open_end_time[dt_p_week_day]:
        print(" KOZOTTE", open_start_time[dt_p_week_day], "<=", hour_rounded, "<=", open_end_time[dt_p_week_day])
        check_open_text = " KOZOTTE" + open_start_time[dt_p_week_day] + "<=" + hour_rounded + "<=" + open_end_time[dt_p_week_day]
        #check_open_text = " KOZOTTE" 
        check_open_boole = True

    #return text_check_open
    checked_start = [start,end,summary,location,check_open_text,check_open_boole] 
    return checked_start


    app.run()