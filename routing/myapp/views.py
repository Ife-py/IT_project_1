from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#example of static routing
def home_view(request):
    return HttpResponse("Welcome to the Home Page")

def about_view(request):
    return HttpResponse("About Us")

def contact_view(request):
    return HttpResponse("Contact Us")