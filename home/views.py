from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts
from features.models import *
from tickets.models import *
from datetime import datetime
from calendar import monthrange
from django.db.models import Max
import calendar

def index(request):
    context = {"index_page":"active"}
    return render(request, 'home.html', context)


def stats(request):
    
    stats_page = "active"
    
    # Get current year
    yearInt = int(datetime.today().strftime('%Y'))

    # Get current month as Int
    monthInt = int(datetime.today().strftime('%m'))
    
    # Set previous month as Int, keeping in mind if month is Jan to revert to month 12
    if monthInt == 1:
        prevMonth = 12
    else:
        prevMonth = monthInt - 1
        
    # Get year date of previous month
    if prevMonth == 12:
        prevMonthYear = yearInt - 1
    else:
        prevMonthYear = yearInt
        
    prevMonthName = calendar.month_name[prevMonth] 
        
    # Total number of days in previous month
    daysInPreviousMonth = monthrange(prevMonthYear, prevMonth)[1]
    
    # Chart 1 - Feature by upvotes
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Votes per Open Feature",
        "xAxisName": "Feature Name",
        "yAxisName": "Upvotes",
        "theme": "candy",
        }
    
    dataSource['data'] = []
    
    for key in Features.objects.all():
        
        if key.status == True:
            data = {}
            data['label'] = key.featurename
            data['value'] = key.upvotes
            dataSource['data'].append(data)


    # Chart 2 - Ticket Dates Test
    
    ticketsDatesSource = {}
    ticketsDatesSource['chart'] = {
        "caption": "Tickets Closed",
        "subcaption": "Per Day",
        "xAxisName": "Day of Month",
        "yAxisName": "Tickets Closed",
        "theme": "candy",
        
    }
    
    ticketsDatesSource['data'] = []
    
    # Stats for month in year
    daysInMonth = monthrange(prevMonthYear, prevMonth)
    
   
    for i in range(1, daysInMonth[1] + 1):
        
        data = {}
        data['label'] = str(i)
        data['value'] = 0
        # ticketsDatesSource['data'].append(data)
        
        for key in Ticket.objects.all():
            time2 = key.closed_date
            
            if time2:
                yearClosed = int(time2.strftime("%Y"))
                monthClosed = int(time2.strftime("%m"))
                dayClosed = int(time2.strftime("%d"))
                strDayClosed = str(dayClosed)
                
                if yearClosed == prevMonthYear and monthClosed == prevMonth:
                    if data['label'] == strDayClosed:
                        value = data['value']
                        value += 1
                        data['value'] = value
                    
        ticketsDatesSource['data'].append(data)
        
        
    # Calculate average tickets closed per day, week and month
    closed_tickets_for_previous_month = 0
    
    # Tickets closed in previous month
    for key in Ticket.objects.all():
        timeClosed = key.closed_date
        
        if timeClosed:
            ticketMonth = int(timeClosed.strftime('%m'))
            ticketYear = int(timeClosed.strftime('%Y'))
            
            if ticketMonth == prevMonth and ticketYear == yearInt:
                closed_tickets_for_previous_month += 1
                
    # Average Tickets closed per day
    averageTicketsPerDay = round((closed_tickets_for_previous_month / daysInPreviousMonth), 2)
    
    # Average Tickets per week
    averageTicketsPerWeek = round((closed_tickets_for_previous_month / 4.345 ), 2)
    
    
    # Charting and rendering of all charts
    column2D = FusionCharts("column2D", "ex1" , "800", "350", "chart-1", "json", dataSource)
    ticketChart = FusionCharts("column2D", "ex2" , "800", "350", "chart-2", "json", ticketsDatesSource)
    
    #Highest upvotes for features if there any open features, else template will show message that no open features with votes
    try:
        most_voted_id = Features.objects.values('id').exclude(status='False').order_by('-upvotes').first()
        most_votes_name = Features.objects.values('featurename').exclude(status='False').order_by('-upvotes').first()
        most_votes = Features.objects.values('upvotes').exclude(status='False').order_by('-upvotes').first()
        votes_name = most_votes_name['featurename']
        votes_total = int(most_votes['upvotes'])
        votes_id = int(most_voted_id['id'])
    except:
        votes_id = False
        votes_name = False
        votes_total = False
    
    return render(request, 'stats.html', {'output': column2D.render(), 'output2': ticketChart.render(), 'votes_id': votes_id, 
        'votes_name': votes_name, 'votes_total': votes_total, 'averageTicketsPerDay': averageTicketsPerDay, 
        'averageTicketsPerWeek': averageTicketsPerWeek, 'closed_tickets_for_previous_month': closed_tickets_for_previous_month, 'stats_page': stats_page,
        'prevMonthName': prevMonthName, 'prevMonthYear': prevMonthYear}) 