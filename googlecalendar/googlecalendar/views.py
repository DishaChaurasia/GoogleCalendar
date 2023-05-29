from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to dishatech")

def contact(request):
    return HttpResponse("12345")

def course(request,courseid):
    return HttpResponse(courseid)