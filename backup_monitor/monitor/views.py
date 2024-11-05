# monitor/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.conf import settings
from pathlib import Path
import datetime
import calendar

@cache_page(60 * 5)  # Cache the view for 5 minutes
@login_required
def calendar_view(request, year=None, month=None):
    # Get the current date
    today = datetime.date.today()
    
    # Determine the year and month to display
    if year and month:
        year = int(year)
        month = int(month)
    else:
        year = today.year
        month = today.month

    # Paths to the backup directories from settings.py
    db_dir = settings.DB_BACKUP_DIR
    www_dir = settings.WWW_BACKUP_DIR

    # Create a calendar object
    cal = calendar.Calendar(firstweekday=0)  # Week starts on Monday (0)
    month_cal = cal.monthdatescalendar(year, month)  # List of weeks in the month

    # Function to get backup dates from a directory
    def get_backup_dates(directory):
        backup_dates = set()
        directory = Path(directory)
        if directory.exists() and directory.is_dir():
            print("DIRECTORY EXISTS")
            for file_path in directory.glob('*.tar.gz'):
                filename = file_path.name
                print(filename)
                try:
                    date_str = filename.rstrip('.tar.gz').split('_')[-1]
                    file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    print(file_date)
                    backup_dates.add(file_date)
                except ValueError:
                    continue
        return backup_dates

    # Get the backup dates for db and www
    db_dates = get_backup_dates(db_dir)
    www_dates = get_backup_dates(www_dir)

    # Create a dictionary to hold information about each date
    date_info = {}
    for week in month_cal:
        for date in week:
            print(date)
            # date_str = date.strftime('%Y-%m-%d')
            date_str = date.isoformat() 
            date_info[date_str] = {
                'has_db': date in db_dates,
                'has_www': date in www_dates,
            }
            print(date_info[date_str])
            print("Date Info Keys:", date_info.keys())

    # List of day names to display in the calendar header
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Calculate previous and next month for navigation
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1

    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    # Context data to pass to the template
    context = {
        'month_name': calendar.month_name[month],
        'year': year,
        'month': month,
        'month_cal': month_cal,
        'date_info': date_info,
        'day_names': day_names,
        'today': today,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    }
    # print(context)

    return render(request, 'monitor/calendar.html', context)
