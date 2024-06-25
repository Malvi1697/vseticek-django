from django.shortcuts import render
from django.http import HttpResponse


def insurance_home(request):
    return HttpResponse("Hello Insurance!")
