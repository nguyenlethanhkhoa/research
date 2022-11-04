from django.shortcuts import render
from django.http import HttpResponse

def get_items(request):
    return HttpResponse('Hello world')
