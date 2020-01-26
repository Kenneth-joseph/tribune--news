from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Moringa School')


def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
        <body>
        <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)


def convert_dates(dates):
    # function that gets the week day number of date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]

    return day


def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
            <html>
                <body>
                    <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
                </body>
            </html>
                '''
    return HttpResponse(html)
