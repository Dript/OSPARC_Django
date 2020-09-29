from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
    	'account':'oSPARC Admin',
    }
    return render(request, 'osparc/index.html', context)

def head_nav(request):
	return render(request, 'osparc/head_nav.html')

	

def list_plants(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/list_plants.html', context)

def add_plant(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/add_plant.html', context)

def plant_added(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/plant_added.html', context)



	





def add_report(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/add_report.html', context)

	

def list_reports(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/list_reports.html', context)

def report_added(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/report_added.html', context)

def help(request):
	context = {
		'account':'oSPARC Admin'
	}
	return render(request, 'osparc/help.html', context)
