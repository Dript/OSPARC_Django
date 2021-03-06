from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^head_nav$', views.head_nav, name='head_nav'),
    url(r'^add_plant$', views.add_plant, name='add_plant'),
    url(r'^plant_added$', views.plant_added, name='plant_added'),
    url(r'^list_plants$', views.list_plants, name='list_plants'),    
    url(r'^list_reports$', views.list_reports, name='list_reports'),
    url(r'^help$', views.help, name='help'),

]
