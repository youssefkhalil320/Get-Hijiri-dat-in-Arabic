import requests
import json
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
def persian_number(persiannumber):
    
    number={
        '0':'۰',
        '1':'۱',
        '2':'۲',
        '3':'۳',
        '4':'٤',
        '5':'٥',
        '6':'٦',
        '7':'۷',
        '8':'۸',
        '9':'۹',
   }

    for i in persiannumber:
        persiannumber= persiannumber.replace(i,number[i])

    return persiannumber

r = requests.get(f"http://api.aladhan.com/v1/gToH?date={day}-{month}-{year}")
j=r.json()
result = j.get('data').get('hijri')
day = result.get('day')
month = result.get('month').get('ar')
day = persian_number(day)
year = result.get('year')
year = persian_number(year)
print(f"اليوم: {day}")
print(f"الشهر : {month}")
print(f"السنة : {year}")
