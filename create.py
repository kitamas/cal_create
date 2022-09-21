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
  "private_key_id": "a982bb94f611bf1fa34d8c42002b26b25f2965dc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDHkkOyFBzn92nq\nQp9dZ933SS6CcQRwfxMzlN4uLkHECAhj3Otkm06e2RmaCaJ1CxE4R8imRD7BHRct\nWNcZMeu3x13FY4/aGUHAKQkXLOK6hnuh7ie06MjTopoHQP1VwuDw4JsIcZ4z/0SK\nZ5X2vCwKlQ8MDwG3+5fNsOnKMEpi9eTZQE7y42HhgVB0ZmuJTjTbmynL2ZxpVsI1\n9WFWfQ915yEA7Lcvpo8KVb0kFkKSOAb64Z8s27Q+GD8nzDCGPgbztSfxvAuoBw00\nwhWdgJV5XZoULfhWImoPVEjw1/JhhGN72Ftvb3jsrniaSyVdFUOR0kCQg9YwnqE3\nXQZL3dYJAgMBAAECggEADdIMuxfWep/xJ0Zu196aCgZ44JKoDoxWTZOpIUSVzFgM\nELJbYM+6jZiWQ8sYA4f9LMsX05/VQrVbhgnpd3a0DrmRPlqrOxzVp1OQLBkxKF6o\n0Cl4eXhHdBSGGyt+f8JrpnK/ecG4hXxPiFAtG/WjDSaOcLTXVyDmvdlbD2PxutGS\nNVXuub98Iw7GHyF2Em46PrAV6iqH1neid+H8MCqU384jlLTxYk/QwmdyDfa8OQ30\ngBK+RpsF5BnIx2zjFnnMQHMYnTSrUsiNblRXPc1iKBEaieX/p+leyKNXSt805uJ0\nnOy1n6ox0zUAhGpfTyX9vd6LKtcCCgz8eFZr1ZjdqQKBgQDkGRYlm2LEwsdx3GB8\nSbuXZx2sdyI5AP173QKc2sp5JsjVxzLaGtSVDdGpxgwBYopDKBZbma4AtX1XRF9m\negm/CgYevRNWmuvG1Bg6Q2y1zgdKiCcG35Lzt+Y82lkTyzfGT+/yqcvdLTfjVbUJ\nXxnHpbCCGH6hfnySSpFwF5T7HQKBgQDf+9zho6OXlv1D0gESeuxnbC4JF28aeXD/\nTYAeIelpaoC6sWs6ZCT5cCpdH6qiqw65ajP2a2xlqGFSXySPa8qI0pDTqLop0J4n\nVSQrf0VCfvV7vb9GpEa3H6pLBnnrIeJ8UlSfPUl/+S02ysFGk+SzvooX9siapZwB\n7uqoKynm3QKBgQCx3kIf51CYwI7IYiI3KUQIZ1eDYo8kRnpkOU7NQ+u5l53q3l/w\nJhX5eYIyUoaQGehZQAxXN7qxQNVR1LZT8fxhpY5qL+TBlyMes8uEu4ktKFEVNKDC\nQluUg6Ydc+MchU6j7TfeUbvwaE95jh8TBL7UqYa/nBw7EKhRZ6aL80ewnQKBgEab\n64HmSEgdfTHIHjZpMeVYoRqUnJ3H8utIzz6wihiFTpeMHrWFpHJN/czlkrE9I6Mn\n68GfE8joT+XbwHbGEE8ZsjZHVoigD3tux7w+nuLbix+7LXVjjDdmcBS+seiCAhgX\nDD4239jMAIjpWgyZytsvEfGEBrFZy9iALNFe6hKxAoGBAIgi6OsdCqAZKu6zd0rz\nh1uPkhcvuNFSzsZKYWH+KgTXcyTFZT+30ul4U+H1tRd2FKlBfjD7GiHzVrnrM6yF\nO3g2dEP1i2/C+U8KeAzfCUxGmQXF7XzXv0N3sWC4kPxW43RdgaICED8x0vv3i9aT\ngxaOnkBfzHvWOIS/TvjD8X8F\n-----END PRIVATE KEY-----\n",
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
    req = request.get_json(force=True)
    print(req)
    #text = "webhook flask text response"
    text = main()

    res = {
        "fulfillment_response": {"messages": [{"text": {"text": [text]}}]}
    }
    return res

@app.route('/createEvent', methods=['GET','POST'])
def createEvent(service, minTime, maxTime):
    try:
        event = {
            "summary": "Google I/O 2022",
            "location": "Budapest",
            "description": "A chance to hear more about Google's developer products.",
            "start": {
                "dateTime": str(minTime),
                "timeZone": "Europe/Budapest",
            },
            "end": {
                "dateTime": str(maxTime),
                "timeZone": "Europe/Budapest",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 24 * 60},
                    {"method": "popup", "minutes": 10},
                ],
            },
        }
        event = (
            service.events()
            .insert(
                calendarId="61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com",
                body=event,
            )
            .execute()
        )
        return "Event created"

    except HttpError as error:
        return "Creation failed"


def main():
    try:
        date = "next-week"
        creds = authentication()
        service = build("calendar", "v3", credentials=creds)
        if date == "next-week":
            cstTimeDelta = datetime.timedelta(hours=1)
            tzObject = datetime.timezone(cstTimeDelta, name="CST")
            dateTime = datetime.datetime.today()
            cstTimeNow = dateTime.replace(tzinfo=tzObject)
            start = cstTimeNow.isoformat("T", "seconds")
            #end = (cstTimeNow + datetime.timedelta(days=7)).isoformat("T", "seconds")
            end = (cstTimeNow + datetime.timedelta(hours=2)).isoformat("T", "seconds")
            #if not overlapCheck(service, start, end):
                #text = createEvent(service, start, end)
            text = createEvent(service, start, end)
            #else:
            #    text = "Overlap detected"
        else:
            text = "Még nincs lekódolva"
    except HttpError as error:
        print("An error occured")
    print(text)

main()

if __name__ == "__main__":

    app.run()