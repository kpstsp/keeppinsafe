from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.conf import settings  # Import settings
import os
import datetime
import calendar

@cache_page(60 * 5)  # Cache the view for 5 minutes
@login_required
def calendar_view(request):
    # Paths to the directories
    db_dir = settings.DB_BACKUP_DIR
    www_dir = settings.WWW_BACKUP_DIR

    
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Generate the month's calendar
    cal = calendar.Calendar()
    month_cal = []
    for week in cal.monthdatescalendar(year, month):
        week_dates = []
        for date in week:
            if date.month == month:
                week_dates.append(date)
            else:
                week_dates.append(None)
        month_cal.append(week_dates)

    # Gather backup file dates
    def get_backup_dates(directory, pattern):
        backup_dates = set()
        for filename in os.listdir(directory):
            if filename.endswith('.tar.gz'):
                try:
                    date_str = filename.rstrip('.tar.gz').split('_')[-1]
                    file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    backup_dates.add(file_date)
                except ValueError:
                    continue
        return backup_dates

    db_dates = get_backup_dates(db_dir, '*_%Y-%m-%d.tar.gz')
    www_dates = get_backup_dates(www_dir, 'sitename.com_%Y-%m-%d.tar.gz')

    # Compile date information
    date_info = {}
    for week in month_cal:
        for date in week:
            if date:
                date_info[date] = {
                    'has_db': date in db_dates,
                    'has_www': date in www_dates,
                }

    context = {
        'month_name': calendar.month_name[month],
        'year': year,
        'month_cal': month_cal,
        'date_info': date_info,
    }
    return render(request, 'monitor/calendar.html', context)
