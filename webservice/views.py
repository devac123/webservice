from django.http import HttpResponse
from django.shortcuts import render

# Simple text response
def home(request):
    return HttpResponse("Hello from Django on Render!")