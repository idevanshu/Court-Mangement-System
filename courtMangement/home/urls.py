from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"), 
    path("services/", views.services, name="services"), 
    path("courtroom/", views.courtRoom, name="courtroom"), 
    path("hearings/", views.hearings, name="hearings"), 
    
]
