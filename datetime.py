            #dt = datetime(2021, 10, 24, 8, 48, 34, 685496)
            #print('Input Datetime:', dt)

            #x = datetime.datetime.today()
            #print("x = datetime.datetime.today()")
            #print(x)
            #d = x.isoformat("T", "seconds")
            #print("ISO 8601 format:", d)


import datetime

dt = datetime(2021, 10, 24, 8, 48, 34, 685496)
print('Input Datetime:', dt)

# convert datetime to ISO date
iso_date = dt.isoformat()
print('ISO Date:', iso_date)