from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def courtRoom(request):
    return HttpResponse("This is courtRoom.")

def services(request):
    return HttpResponse("<h1>CourtROOM services</h1>")

def hearings(request):
    return HttpResponse("<h1>Courtroom hearings</h1>")