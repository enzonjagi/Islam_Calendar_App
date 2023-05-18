from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
import requests

def hijri_today(request):
    """We'll use this to consume the Hijri calendar api
    
    Find more info: 
        * https://aladhan.com/islamic-calendar-api
    """

    parsed_date = []
    # pulling data for the current date
    # to convert today's date to HijriCalendar Date
    today_response = requests.get(
        'http://api.aladhan.com/v1/gToH/16-05-2023'
    )

    # let's convert this to JSON
    today = today_response.json()

    return render(request, "today.html", {'today': today})
def hijri_month(request):
    """The goal of this function is to create a view of the whole month requested
    
    Process:
        1. Create forms for user to specify Gregorian month number and year
        2. Use this month and year to make a api call and pull data
            * Append the month and date to the necessary parts of the api call
        3. Display the month name at the top of the page
        4. Call the hijri_day function to give us the days of that month
        5. Fill in the days of the month to the created Month table.
    """
    
    #TODO Start from step 4 and start by answering the following question: 
    #   * How do we add numbers to the end of a url in Django?
    #   * How do we use this number as input for the month_num variable?

    # we'll start with default values then add a feature to allow user to change these:
    # USer can supply month number in url or in a form on the page
    year_num = 2023
    url = f'http://api.aladhan.com/v1/gToHCalendar/{1}/{year_num}'

    # pull the data
    month = requests.get(url)

    # convert the month to JSON
    month_data = month.json()

    return render(request, "month.html", {'month': month_data})