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

    check_wd_open_ret = check_wd_open()
    check_wd_open_txt = check_wd_open_ret[4]
    start_p =  check_wd_open_ret[0]
    end_p =  check_wd_open_ret[1]
    summary =  check_wd_open_ret[2]
    location =  check_wd_open_ret[3]

    boolean_wd_open =  check_wd_open_ret[5]
    dt_p_obj_rounded  =  check_wd_open_ret[6]
    duration =  check_wd_open_ret[7]
    hours_am =  check_wd_open_ret[8]

    # print("start_p = ", check_wd_open_ret[0])
    # print("end_p  =", check_wd_open_ret[1])
    # print("boolean_wd_open = ", check_wd_open_ret[5])
    # print("dt_p_obj_rounded = ", dt_p_obj_rounded)

    """
    free_busy_text = free_busy(dt_p_obj_rounded,duration)
    """

    if boolean_wd_open:     
        get_events_ret = get_events(dt_p_obj_rounded,duration)
        print("GET EVENTS RET  = ",get_events_ret)

        if get_events_ret == 'free':
            boolean_get_events = True
        else:
            boolean_get_events = False
    else:
        check_wd_open_txt = "ZÁRVA" 
        get_events_ret = "nincs esemeny"


    if boolean_wd_open and boolean_get_events:
        main_ret =  main(start_p,end_p,summary,location)    


    get_events_gaps_ret = get_events_gaps(dt_p_obj_rounded,duration)
    print("GET EVENTS GAPS RET  = ",get_events_gaps_ret)

    #text = main_ret['text'] + check_wd_open_txt + " B_1wd= " + str(check_wd_open_ret[5]) + " | " + get_events_ret + " | B_ev= " + str(boolean_get_events) + " hours_am:" + str(hours_am)
    text = " | " + check_wd_open_txt + " | " + get_events_ret

    # event_id = main_ret['event_id']
    event_id = 'event_id'

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


def main(start_p,end_p,summary,location):

    start = start_p
    # 2022-10-09T12:00:00

    #end = (dt_p_obj + datetime.timedelta(hours=1)).isoformat("T", "seconds")
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
    # !!!!! timeZone": "Europe/Budapest" !!!!! start hour + 1

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
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    # return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + datetime.timedelta(hours=t.minute // 30))

    # Rounds to next hour by adding a timedelta hour + 1

    if t.minute != 0:
        return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour + 1))
    else:
        return (t.replace(second=0, microsecond=0, minute=0))


def check_wd_open():
    current_dateTime = datetime.datetime.now() + datetime.timedelta(hours=1)

    req = request.get_json(force=True)
    # print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')

    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')

    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    open_start_time = ["10:00", "09:00", "10:00", "11:00", "08:00", "13:00", "11:00"]
    open_end_time = ["19:00", "19:00", "19:00", "18:00", "17:00", "19:00", "19:00"]

    week_days = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")

    dt_p_string = str(int(year)) + "," + str(int(month)) + "," + str(int(day)) + "," + str(int(hours)) + "," + str(int(minutes))
    # DATE TIME PARAMETERS STRING:  2022,10,9,12,0

    dt_p_obj = datetime.datetime.strptime(dt_p_string, '%Y,%m,%d,%H,%M')
    # 2022-09-25 00:00:00 - string to datetime object

    hours_am = am_pm_conv(current_dateTime,dt_p_obj,hours)

    dt_p_week_day = dt_p_obj.weekday()
    dt_p_week_day_name = week_days[dt_p_week_day]
    print("dt_p_week_day_name:", dt_p_week_day_name)

    dt_p_obj_rounded = hour_rounder(dt_p_obj)

    # hour_rounded = dt_p_obj_rounded
    # print("DT PARAM OBJ HOUR ROUNDED:", dt_p_obj_rounded,type(dt_p_obj_rounded))
    # 2022-10-31 21:00:00 <class 'datetime.datetime'>

    start_p = dt_p_obj_rounded.isoformat("T", "seconds")
    # print("START from parameter ROUNDED= ",start_p,type(start_p))

    duration = datetime.timedelta(hours=1)

    #end_p = (dt_p_obj + datetime.timedelta(hours=1)).isoformat("T", "seconds")
    end_p = (dt_p_obj + duration).isoformat("T", "seconds")


    if current_dateTime > dt_p_obj:
        print("A ",dt_p_obj,"idő már elmúlt. A jelenlegi idő:",current_dateTime,"Adjon meg másik időpontot.")
        check_wd_open_text = " A " + dt_p_obj.strftime('%H:%M') + " idő már elmúlt. A jelenlegi idő: " + current_dateTime.strftime('%H:%M') +  " Adjon meg másik időpontot."
        boolean_wd_open = False

        check_wd_open_ret = [start_p,end_p,summary,location,check_wd_open_text,boolean_wd_open,dt_p_obj_rounded,duration,hours_am]  
        return check_wd_open_ret

    # print("open_start_time:", open_start_time[dt_p_week_day])
    # print("open_end_time:", open_end_time[dt_p_week_day])

    # open_start_time[dt_p_week_day] = 10:00 <class 'str'>
    # print("HOUR open_start_time[dt_p_week_day][0:2]",open_start_time[dt_p_week_day][0:2])
    # print("MINUTE open_start_time[dt_p_week_day][3:5]",open_start_time[dt_p_week_day][3:5])

    # print("STRP open_start_time[dt_p_week_day] = ",dt_p_obj.replace(minute=0, hour=int(open_start_time[dt_p_week_day][0:2])))

    start_pdate_otime = dt_p_obj.replace(minute=0, hour=int(open_start_time[dt_p_week_day][0:2]))
    # day: parameter date, open start time, obj

    end_pdate_otime = dt_p_obj.replace(minute=0, hour=int(open_end_time[dt_p_week_day][0:2]))
    # day: parameter date, end start time, obj

    # print("start_pdate_otime =", start_pdate_otime)
    # print("end_pdate_otime = ", end_pdate_otime)


    if dt_p_obj_rounded < start_pdate_otime:
        print("KORÁN", dt_p_obj_rounded, "<", start_pdate_otime)
        check_wd_open_text = " KORÁN. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        boolean_wd_open = False

    if dt_p_obj_rounded >= end_pdate_otime:
        print("KÉSŐN", dt_p_obj_rounded, ">=", end_pdate_otime)
        check_wd_open_text = " KÉSŐN. " + dt_p_week_day_name + " nyitás: " + open_start_time[dt_p_week_day] + " zárás: " + open_end_time[dt_p_week_day]
        boolean_wd_open = False

    if dt_p_obj_rounded >= start_pdate_otime and dt_p_obj_rounded + duration <= end_pdate_otime:
        print("hour rounded + duration = ",dt_p_obj_rounded + duration)
        print(" KOZOTTE", open_start_time[dt_p_week_day], "<=", dt_p_obj_rounded + duration, "<=", open_end_time[dt_p_week_day])
        #check_wd_open_text = open_start_time[dt_p_week_day] + " <= " + dt_p_obj_rounded.strftime("%B %A %H:%M") + " <= " + open_end_time[dt_p_week_day]
        check_wd_open_text = " NYITVA "
        boolean_wd_open = True

    check_wd_open_ret = [start_p,end_p,summary,location,check_wd_open_text,boolean_wd_open,dt_p_obj_rounded,duration,hours_am] 
    return check_wd_open_ret


#def get_events(start_p,end_p):
def get_events(dt_p_obj_rounded,duration):

    try:
        service = build('calendar', 'v3', credentials=authentication())

        # calendar: szemeszet 12:00, gumi 13:00 
        # list start_p 12:00: ONLY ONE EVENT: gumi 13:00
        # list start_p 11:59: TWO EVENTS: szemeszet 12:00, gumi 13:00
  
        # HOUR:00 - min1 = (HOUR-1):59   

        min1 = datetime.timedelta(minutes=1)

        start_p_min1 = (dt_p_obj_rounded - min1).isoformat("T", "seconds")
        start_p = start_p_min1 + '+00:00'
        print("GET EVENTS START P = ",start_p)

        end_p1 = (dt_p_obj_rounded).isoformat("T", "seconds")
        # lists the next hour event !!!
        # end_p1 = (dt_p_obj_rounded + min1).isoformat("T", "seconds")
        # end_p1 = (dt_p_obj_rounded + duration - min1).isoformat("T", "seconds")
        # lists the next hour event !!!

        end_p = end_p1 + '+00:00'
        print("GET EVENTS END P = ",end_p)

        events_result = service.events().list(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com', timeMin=start_p,timeMax=end_p,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # print(json.dumps(events, indent=4))

        if not events:
            print('free')
            start_event = 'free'

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
        start = start2.strftime("%B %A %H:%M")

        start_event = "FOGLALT: " + events[0]['summary'] + " "  + start + " | "
        print("only the first element of the list =",start_event)

        return start_event

    except HttpError as error:
        print('An error occurred: %s' % error)


def get_events_gaps(dt_p_obj_rounded,duration):

    try:
        service = build('calendar', 'v3', credentials=authentication())

        min1 = datetime.timedelta(minutes=1)

        start_p_min1 = (dt_p_obj_rounded - min1).isoformat("T", "seconds")
        start_p = start_p_min1 + '+00:00'
        print("GET EVENTS GAPS START P = ",start_p)

        duration = datetime.timedelta(hours=10)

        end_p1 = (dt_p_obj_rounded + duration).isoformat("T", "seconds")

        end_p = end_p1 + '+00:00'
        print("GET EVENTS GAPS END P = ",end_p)

        events_result = service.events().list(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com', timeMin=start_p,timeMax=end_p,
                                              maxResults=8, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # print(json.dumps(events, indent=4))

        if not events:
            print('free')
            start_event = 'free'

            return start_event

        # = = = = = = = = = = = = = = = = = = = = = = 
        # startTime = datetime.datetime.now() + datetime.timedelta(hours = 1)
        startTime = dt_p_obj_rounded
        # startTime = startTime - min1

        print("startTime GAPS = = = = = ",startTime)

        endTime = datetime.datetime(2022, 11, 12, 23, 59, 59, 0)

        print("endTime GAPS = = = = =",endTime)

        duration = datetime.timedelta(hours = 1)

        f_obj = findFirstOpenSlot(events,startTime,endTime,duration)
        if f_obj == "None":
            f_time = "NINCS"
        else:
            print("f_obj = ",f_obj)
            f_time = f_obj.strftime("%Y-%m-%d %H:%M")

        firsto = "FIRST OPEN: "        
        print(firsto,f_time)

        # only the first element of the list

        start1 = events[0]['start'].get('dateTime', events[0]['start'].get('date'))
        start2 = datetime.datetime.strptime(start1,'%Y-%m-%dT%H:%M:%S%z')
        start = start2.strftime("%B %A %H:%M")

        start_event = events[0]['summary'] + " "  + start + " | "
        print("GAPS GAPS only the first element of the list =",start_event)

        return start_event


    except HttpError as error:
        print('An error occurred: %s' % error)


def am_pm_conv(current_dateTime,dt_p_obj,hours):
    # print("hours = ",hours)
    # print("current_dateTime.hour = ",current_dateTime.hour)
    # print("dt_p_obj = ",dt_p_obj)

    if current_dateTime.hour < 12  and dt_p_obj > current_dateTime :
        hours_am = hours - 12
    else:
        hours_am = hours
    return hours_am


def findFirstOpenSlot(events,startTime,endTime,duration):

    def parseDate(rawDate):
        # RAWDATE =  2022-10-17T09:00:00Z
        # Transform the datetime given by the API to a python datetime object.
        # return datetime.datetime.strptime(rawDate[:-6]+ rawDate[-6:].replace(":",""), '%Y-%m-%dT%H:%M:%S%z')

        # return datetime.datetime.strptime(rawDate, '%Y-%m-%dT%H:%M:%SZ')
        # GMT + 2  = return datetime.datetime.strptime(rawDate,'%Y-%m-%dT%H:%M:%S+02:00')

        return datetime.datetime.strptime(rawDate,'%Y-%m-%dT%H:%M:%S+01:00')

    eventStarts = [parseDate(e['start'].get('dateTime', e['start'].get('date'))) for e in events]

    eventEnds = [parseDate(e['end'].get('dateTime', e['end'].get('date'))) for e in events]

    print("EVENT ENDS eventEnds = ", eventEnds)
    # eventEnds = [datetime.datetime(2022, 10, 24, 18, 0), datetime.datetime(2022, 10, 24, 20, 0), datetime.datetime(2022, 10, 24, 22, 0)]  LIST [datetime]
    # eventEnds[0] = 2022-10-24 18:00:00

    print("LEN EVENTENDS=",len(eventEnds))

    free_start_hours = ""
    for i in range(len(eventEnds)):
        free_start_hour = str(eventEnds[i].hour) + ", "
        free_start_hours += free_start_hour
    print("FREE START HOURS =",free_start_hours)

    gaps = [start-end for (start,end) in zip(eventStarts[1:], eventEnds[:-1])]

    # print("GAPS = ",gaps)
    # GAPS =  [datetime.timedelta(seconds=3600), datetime.timedelta(seconds=3600)]
    # print("enumerate(gaps) =",enumerate(gaps))
    # enumerate(gaps) = <enumerate object at 0x7f4527c24140>

    print("FIRST OPEN START = ",eventEnds[0])
    # FIRST OPEN START =  2022-10-24 17:00:00

    # if ROUNDED startTime + duration < eventStarts[0]:
    if startTime + duration < eventStarts[0]:
        # A slot is open at the start of the desired window.
        return startTime

    for i, gap in enumerate(gaps):
        if gap >= duration:
        #This means that a gap is bigger or = than the desired slot duration, and we can "squeeze" a meeting. Just after that meeting ends.
        #if gap > duration:
        #This means that a gap is bigger than the desired slot duration

            # print("i = ",i," eventEnds[i] = ", eventEnds[i])
            # i =  1  eventEnds[i] =  2022-11-12 16:00:00 <class 'datetime.datetime'>

            return eventEnds[i]

    #If no suitable gaps are found, return none.
    return "None"
    
    app.run()

"""
def free_busy(dt_p_obj_rounded,duration):

    try:
        service = build('calendar', 'v3', credentials=authentication())

        min1 = datetime.timedelta(minutes=1)

        start_p_min1 = (dt_p_obj_rounded - min1).isoformat("T", "seconds")
        start_p = start_p_min1 + '+00:00'
        print("FREE BUSY START P = ",start_p)

        end_p1 = (dt_p_obj_rounded).isoformat("T", "seconds")
        end_p = end_p1 + '+00:00'
        print("FREE BUSY END P = ",end_p)

        body = {
                "timeMin": start_p,
                "timeMax": end_p,
                "timeZone": 'Europe/Budapest',
                "items": [{"id": '61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com'}]
               }

        event_result = service.freebusy().query(body=body).execute()

        # print(json.dumps(event_result, indent=4))

        free_busy_text = str(event_result['calendars']['61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com']['busy'])

        return free_busy_text

    except HttpError as error:
        print('An error occurred: %s' % error)
"""