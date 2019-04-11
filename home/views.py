from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts
from features.models import *
from tickets.models import *
import datetime
from calendar import monthrange

def index(request):
    return render(request, 'home.html')


def stats(request):
    
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
    
    # Stats for March 2019
    daysInMonth = monthrange(2019, 3)
    
   
    for i in range(1, daysInMonth[1] + 1):
        
        data = {}
        data['label'] = str(i)
        data['value'] = 0
        # ticketsDatesSource['data'].append(data)
        
        for key in Ticket.objects.all():
            time2 = key.closed_date
            
            if time2:
                dayClosed = int(time2.strftime("%m"))
                strDayClosed = str(dayClosed)
                
                if data['label'] == strDayClosed:
                    value = data['value']
                    value += 1
                    data['value'] = value
                    
        ticketsDatesSource['data'].append(data)
        

    # Charting and rendering of all charts
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    ticketChart = FusionCharts("column2D", "ex2" , "600", "350", "chart-2", "json", ticketsDatesSource)
    return render(request, 'stats.html', {'output': column2D.render(), 'output2': ticketChart.render()}) 