from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import employee,admin,employeedash

app.route('/employee-dash')
def show_employee():
    return render_template('employeedash.html')

# def homepage(request):

#     NewChart = employeedash()
#     NewChart.data.label = "My Favourite Numbers"      # can change data after creation

#     ChartJSON = NewChart.get()

#     return render_template(request=request,
#                   template_name='main/home.html',
#                   context={"chartJSON": ChartJSON})