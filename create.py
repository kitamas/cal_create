# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request

# CRED = = = = = = = = = = =
import googleapiclient.discovery
from google.oauth2 import service_account as google_oauth2_service_account

# QUICKSTART = = = = = = = = = = =
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import time

import locale
 # locale.setlocale(locale.LC_ALL, "HU_hu.utf8")
 # locale.setlocale(locale.LC_TIME, "HU_hu.utf8")
 # print("LOCALE LOCALE",current_dateTime.strftime('%A, %a, %B, %b'))

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
    print("FUNCTION WEBHOOK")

    wd_open_ret = wd_open()

    start_p =  wd_open_ret[0]
    end_p =  wd_open_ret[1]
    summary =  wd_open_ret[2]
    location =  wd_open_ret[3]
    wd_open_txt = wd_open_ret[4]
    wd_open_boolean =  wd_open_ret[5]
    start_dt_p_obj_rounded  =  wd_open_ret[6]
    end_dt_p_obj  =  wd_open_ret[7]
    duration =  wd_open_ret[8]
    hours_am =  wd_open_ret[9]

    # print("start_p = ", wd_open_ret[0], " end_p = ", wd_open_ret[1], " wd_open_boolean = ", wd_open_ret[5], " start_dt_p_obj_rounded = ", start_dt_p_obj_rounded)

    get_events_gaps_ret = ""
    event_id = ""

    if wd_open_boolean:     
        print("IF WD OPEN BOOLEAN")

        get_events_ret = get_events(start_dt_p_obj_rounded,duration)
        get_events_ret_txt = get_events_ret[0]
        get_events_ret_boolean = get_events_ret[1]

        # boolean_get_events = True = Szabad

        print("IF WD_OPEN_BOOLEAN. get_events_ret_txt = ",get_events_ret[0],"get_events_ret_boolean = ",get_events_ret[1])
        # IF WD_OPEN_BOOLEAN. get_events_ret_txt =   nincs esemény az időpontban  get_events_ret_boolean =  True

        if get_events_ret_boolean:
            print("IF WD_OPEN_BOOLEAN = ", wd_open_boolean ," AND GET_EVENTS_RET_BOOLEAN = ",get_events_ret[1])

            main_ret =  create_event_main(start_p,end_p,summary,location)    
            event_id = main_ret['event_id']
            print("if get_events_ret_boolean = main_ret =  create_event_main")

        else:
            get_events_gaps_ret = " Foglalt gaps időpont(ok): " + get_events_gaps(start_dt_p_obj_rounded,end_dt_p_obj,duration)
            print("GET EVENTS GAPS RET get_events_gaps_ret = ",get_events_gaps_ret)

    else:
        print("IF WD OPEN BOOLEAN ELSE. wd zárva, nem kérdez eseményt. ")
        get_events_ret_txt = " wd zárva, nem kérdez eseményt. "
        get_events_ret_boolean = False
        # KELL? get_events_ret_boolean = False
    
    # text = wd_open_txt + " hours_am:" + str(hours_am)
    text = wd_open_txt + get_events_ret_txt + get_events_gaps_ret + "event_id: " + event_id

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
                "event_id" : event_id,
                "wd_open" : str(wd_open_boolean),
                "free_busy" : str(get_events_ret_boolean)
            }
        }
    }

    return res


def create_event_main(start_p,end_p,summary,location):
    print("FUNCTION create_event_main")
    start = start_p
    # 2022-10-09T12:00:00

    #end = (start_dt_p_obj + datetime.timedelta(hours=1)).isoformat("T", "seconds")
    end = end_p

    creds = authentication()
    service = build("calendar", "v3", credentials=creds)

    # sendUpdates='all' -> sending email
    # event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',sendUpdates='all',

    event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',
       body={
           "summary": summary,
           "location": location,
           "description": "This is the description (parkolo/targyalo, stb)",
           "start": {"dateTime": start,"timeZone": "Europe/Budapest"},
           "end": {"dateTime": end,"timeZone": "Europe/Budapest"},
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
    # timeZone": "Europe/Budapest" -> hour = hour + 1

    start_event = datetime.datetime.strptime(event_result['start']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')
    end_event = datetime.datetime.strptime(event_result['end']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')

    #start_event = datetime.datetime.strptime(event_result['start']['dateTime'],'%Y-%m-%dT%H:%M')
    #end_event = datetime.datetime.strptime(event_result['end']['dateTime'],'%Y-%m-%dT%H:%M')

    text = "Kezdő időpont: " + start_event.strftime("%B %A %H:%M") + " Vége: " + end_event.strftime("%B %A %H:%M") + " "

    main_ret = {}
    main_ret['text'] = text
    main_ret['event_id'] = event_result['id']
  
    return main_ret


def hour_rounder(t):
    print("FUNCTION hour_rounder")
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    # return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + datetime.timedelta(hours=t.minute // 30))

    # Rounds to next hour by adding a timedelta hour + 1

    if t.minute != 0:
        return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour + 1))
    else:
        return (t.replace(second=0, microsecond=0, minute=0))


def wd_open():
    print("FUNCTION wd_open")
    current_dateTime = datetime.datetime.now() + datetime.timedelta(hours=1)

    req = request.get_json(force=True)
    # print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')
    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    # HOURS ORIGINAL FROM USER hours_original = req.get('intentInfo').get('parameters').get('time').get('originalValue')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')
    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    open_start_time = ["08:00", "09:00", "08:00", "08:00", "08:00", "08:00", "08:00"]
    open_end_time = ["17:00", "22:00", "21:00", "21:00", "17:00", "16:00", "12:00"]

    week_days = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")

    start_dt_p_string = str(int(year)) + "," + str(int(month)) + "," + str(int(day)) + "," + str(int(hours)) + "," + str(int(minutes))
    # DATE TIME PARAMETERS STRING:  2022,10,9,12,0

    start_dt_p_obj = datetime.datetime.strptime(start_dt_p_string, '%Y,%m,%d,%H,%M')
    # 2022-09-25 00:00:00 - string to datetime object

    # Dialogflow am - pm converter (10:00 <-> 22:00)
    # hours_am = am_pm_conv(current_dateTime,start_dt_p_obj,hours)
    hours_am = "hours_am"

    dt_p_week_day = start_dt_p_obj.weekday()
    dt_p_week_day_name = week_days[dt_p_week_day]
    # print("dt_p_week_day_name:", dt_p_week_day_name)

    start_dt_p_obj_rounded = hour_rounder(start_dt_p_obj)

    # print("START DT PARAM OBJ ROUNDED = ", start_dt_p_obj_rounded,type(start_dt_p_obj_rounded))
    # 2022-10-31 21:00:00 <class 'datetime.datetime'>

    start_p = start_dt_p_obj_rounded.isoformat("T", "seconds")
    # print("START from parameter ROUNDED = start_p = ",start_p,type(start_p))

    duration = datetime.timedelta(hours=1)

    # create end_wd_open_obj (end weekday open time obj)
    # print("open_end_time[dt_p_week_day] = ", open_end_time[dt_p_week_day], type(open_end_time[dt_p_week_day]))
    # print("HOUR open_end_time[dt_p_week_day][0:2]",open_end_time[dt_p_week_day][0:2])
    # print("MINUTE open_end_time[dt_p_week_day][3:5]",open_end_time[dt_p_week_day][3:5])

    end_wd_open_obj = start_dt_p_obj.replace(minute=0, hour=int(open_end_time[dt_p_week_day][0:2]))
    # end_wd_open_obj =  2022-11-16 17:00:00 <class 'datetime.datetime'>

    end_p = (start_dt_p_obj + duration).isoformat("T", "seconds")
    # end_p =  2022-11-16T17:00:00

    if current_dateTime > start_dt_p_obj:
        print("A ",start_dt_p_obj,"idő már elmúlt. A jelenlegi idő:",current_dateTime)
        wd_open_text = " A " + start_dt_p_obj.strftime('%H:%M') + " idő már elmúlt. A jelenlegi idő: " + current_dateTime.strftime('%H:%M') + "."
        wd_open_boolean = False

        wd_open_ret = [start_p,end_p,summary,location,wd_open_text,wd_open_boolean,start_dt_p_obj_rounded,end_wd_open_obj,duration,hours_am]  
        return wd_open_ret

    # open time and closed time on parameter day
    start_pdate_otime = start_dt_p_obj.replace(minute=0, hour=int(open_start_time[dt_p_week_day][0:2]))
    end_pdate_otime = start_dt_p_obj.replace(minute=0, hour=int(open_end_time[dt_p_week_day][0:2]))
    # start_pdate_otime = 2022-11-16 08:00:00


    if start_dt_p_obj_rounded < start_pdate_otime:
        # print("KORÁN", start_dt_p_obj_rounded, "<", start_pdate_otime)
        wd_open_text = " Korán. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        wd_open_boolean = False

    if start_dt_p_obj_rounded >= end_pdate_otime:
        # print("KÉSŐN", start_dt_p_obj_rounded, ">=", end_pdate_otime)
        wd_open_text = " Késő. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        wd_open_boolean = False

    if start_dt_p_obj_rounded >= start_pdate_otime and start_dt_p_obj_rounded + duration <= end_pdate_otime:
        # print(" KOZOTTE", open_start_time[dt_p_week_day], "<=", start_dt_p_obj_rounded + duration, "<=", open_end_time[dt_p_week_day])
        # wd_open_text = open_start_time[dt_p_week_day] + " <= " + start_dt_p_obj_rounded.strftime("%B %A %H:%M") + " <= " + open_end_time[dt_p_week_day]
        # wd_open_text = " Nyitva. "
        wd_open_text = " "
        wd_open_boolean = True

    wd_open_ret = [start_p,end_p,summary,location,wd_open_text,wd_open_boolean,start_dt_p_obj_rounded,end_wd_open_obj,duration,hours_am]

    return wd_open_ret


#def get_events(start_p,end_p):
def get_events(start_dt_p_obj_rounded,duration):
    print("FUNCTION get_events")
    try:
        service = build('calendar', 'v3', credentials=authentication())

        # calendar: szemeszet 12:00, gumi 13:00 
        # list start_p 12:00: ONLY ONE EVENT: gumi 13:00
        # list start_p 11:59: TWO EVENTS: szemeszet 12:00, gumi 13:00
  
        # HOUR:00 - min1 = (HOUR-1):59   

        min1 = datetime.timedelta(minutes=1)

        start_p_min1 = (start_dt_p_obj_rounded - min1).isoformat("T", "seconds")
        start_p = start_p_min1 + '+00:00'
        # print("GET EVENTS START P = ",start_p)

        end_p1 = (start_dt_p_obj_rounded).isoformat("T", "seconds")
        # lists the next hour event !!!
        # end_p1 = (start_dt_p_obj_rounded + min1).isoformat("T", "seconds")
        # end_p1 = (start_dt_p_obj_rounded + duration - min1).isoformat("T", "seconds")
        # lists the next hour event !!!

        end_p = end_p1 + '+00:00'
        # print("GET EVENTS END P = ",end_p)

        events_result = service.events().list(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com', timeMin=start_p,timeMax=end_p,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # print(json.dumps(events, indent=4))

        if not events:
            boolean_get_events = True
            start_event_txt = ' nincs esemény az időpontban '
            start_event = [start_event_txt,boolean_get_events]

            return start_event

        """
        start_event = "" 
        for event in events:
            start1 = event['start'].get('dateTime', event['start'].get('date'))
            start2 = datetime.datetime.strptime(start1,'%Y-%m-%dT%H:%M:%S%z')
            start = start2.strftime("%B %A %H:%M")

            start_event += event['summary'] + " "  + start + " | "
        """

        # only the first element of the list

        start1 = events[0]['start'].get('dateTime', events[0]['start'].get('date'))
        start2 = datetime.datetime.strptime(start1,'%Y-%m-%dT%H:%M:%S%z')
        #start = start2.strftime("%B %A %H:%M")
        start = start2.strftime("%H:%M")

        start_event_txt = "Foglalt. " + events[0]['summary'] + " "  + start
        # start_event_txt = start + " időpont foglalt. " 
        # print("only the first element of the list =",start_event_txt)
        print("IDOPONT FOGLALT",start_event_txt)

        boolean_get_events = False
        start_event = [start_event_txt,boolean_get_events]
        return start_event

    except HttpError as error:
        print('An error occurred: %s' % error)


def get_events_gaps(start_dt_p_obj_rounded,end_wd_open_obj,duration):
    print("FUNCTION get_events_gaps")
    try:
        service = build('calendar', 'v3', credentials=authentication())

        min1 = datetime.timedelta(minutes=1)

        start_p_min1 = (start_dt_p_obj_rounded - min1).isoformat("T", "seconds")
        start_p = start_p_min1 + '+00:00'

        # end_p1 = (end_wd_open_obj - duration).isoformat("T", "seconds")
        end_p1 = (end_wd_open_obj).isoformat("T", "seconds")
        end_p = end_p1 + '+00:00'
        print("GET EVENTS GAPS END P = ",end_p)

        events_result = service.events().list(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com', timeMin=start_p,timeMax=end_p,
                                              maxResults=8, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # print(json.dumps(events, indent=4))

        if not events:
            print('NO EVENTS NO EVENTS get_event_gaps = no events')
            start_event = 'get_event_gaps = start_events = no events'

            return start_event

        # startTime = datetime.datetime.now() + datetime.timedelta(hours = 1)
        # startTime = startTime - min1
        startTime = start_dt_p_obj_rounded
        print("startTime = start_dt_p_obj_rounded = ",startTime)

        # endTime = datetime.datetime(2022, 11, 12, 23, 59, 59, 0)

        endTime = end_wd_open_obj
        print("endTime = end_wd_open_obj = ",endTime)

        duration = datetime.timedelta(hours = 1)

        findFirstOpenSlot_ret = findFirstOpenSlot(events,startTime,endTime,duration)
        print("findFirstOpenSlot_ret = ",findFirstOpenSlot_ret,type(findFirstOpenSlot_ret))

        if findFirstOpenSlot_ret == "None":
            f_time = "NINCS"
        else:
            print("ELSE findFirstOpenSlot_ret = ",findFirstOpenSlot_ret)
            # f_time = f_obj.strftime("%Y-%m-%d %H:%M")
            f_time = findFirstOpenSlot_ret

        print("findFirstOpenSlot_ret = ",findFirstOpenSlot_ret)

        return findFirstOpenSlot_ret

    except HttpError as error:
        print('An error occurred: %s' % error)


def am_pm_conv(current_dateTime,start_dt_p_obj,hours):
    # print("hours = ",hours)
    # print("current_dateTime.hour = ",current_dateTime.hour)
    # print("start_dt_p_obj = ",start_dt_p_obj)

    if current_dateTime.hour < 12  and start_dt_p_obj > current_dateTime :
        hours_am = hours - 12
    else:
        hours_am = hours
    return hours_am


def findFirstOpenSlot(events,startTime,endTime,duration):
    print("FUNCTION findFirstOpenSlot. startTime = ",startTime,"endTime = ", endTime)
    def parseDate(rawDate):
        # RAWDATE =  2022-10-17T09:00:00Z
        # Transform the datetime given by the API to a python datetime object.
        # return datetime.datetime.strptime(rawDate[:-6]+ rawDate[-6:].replace(":",""), '%Y-%m-%dT%H:%M:%S%z')

        # return datetime.datetime.strptime(rawDate, '%Y-%m-%dT%H:%M:%SZ')
        # GMT + 2  = return datetime.datetime.strptime(rawDate,'%Y-%m-%dT%H:%M:%S+02:00')

        return datetime.datetime.strptime(rawDate,'%Y-%m-%dT%H:%M:%S+01:00')

    eventStarts = [parseDate(e['start'].get('dateTime', e['start'].get('date'))) for e in events]

    eventEnds = [parseDate(e['end'].get('dateTime', e['end'].get('date'))) for e in events]

    print("EVENT STARTS EVENT STARTS eventStarts = ", eventStarts)
    print("EVENT ENDS EVENT ENDS eventEnds = ", eventEnds)
    # eventEnds = [datetime.datetime(2022, 10, 24, 18, 0), datetime.datetime(2022, 10, 24, 20, 0), datetime.datetime(2022, 10, 24, 22, 0)]  LIST [datetime]
    # eventEnds[0] = 2022-10-24 18:00:00

    """
    free_start_hours = ""
    for i in range(len(eventEnds)):
        free_start_hour = str(eventEnds[i].hour) + ", "
        free_start_hours += free_start_hour
    print("FREE START HOURS =",free_start_hours)
    """

    busy_start_hours = ""
    for i in range(len(eventStarts)):
        busy_start_hour = str(eventStarts[i].hour) + ", "
        busy_start_hours += busy_start_hour
    print("BUSY START HOURS =",busy_start_hours)

    gaps = [start-end for (start,end) in zip(eventStarts[1:], eventEnds[:-1])]

    print("GAPS = ",gaps,"type gaps = ",type(gaps),"len(gaps) =",len(gaps), "type(len(gaps))=",type(len(gaps)))
    # GAPS =  [datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600)]  type gaps =  <class 'list'> len(gaps) = 1 type(len(gaps))= <class 'int'>
 
    print("enumerate(gaps) =",enumerate(gaps))
    # enumerate(gaps) = <enumerate object at 0x7f4527c24140>

    # print("FIRST OPEN START = ",eventEnds[0])
    # FIRST OPEN START =  2022-10-24 17:00:00

    # if ROUNDED startTime + duration < eventStarts[0]:
    # KELL ez? 
    if startTime + duration < eventStarts[0]:
        # A slot is open at the start of the desired window.
        print("11111 if startTime + duration < eventStarts. return startTime", startTime)
        # return startTime
        return "startTime"

    """
    # for i in range(len(gaps)):
    for i, gap in enumerate(gaps):
        if gap >= duration:
    """
    ts = ""
    for i in range(len(gaps)):

        if gaps[i] >= duration:

        # This means that a gap is bigger or = than the desired slot duration, and we can "squeeze" a meeting. Just after that meeting ends.
        # if gap > duration:
        # This means that a gap is bigger than the desired slot duration

            print("22222 i = ",i," eventStarts[i] = ", eventStarts[i])
            # i =  1  eventEnds[i] =  2022-11-12 16:00:00 <class 'datetime.datetime'>

            t = eventStarts[i].strftime("%B %A %H:%M") + "FOR"
            ts += t 
            print("BBBBB ts=",ts,"type(ts)=",type(ts))
            eventStarts[i] = " eventStarts[i] = " + ts
    return eventStarts[i]

    # If no suitable gaps are found, return none.
    # print("33333 If no suitable gaps are found, return none.")
    return " If no suitable gaps are found, return none. "
    # return "busy_start_hours: " + busy_start_hours

    app.run()