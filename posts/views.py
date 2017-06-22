from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post(request):
    return HttpResponse(r"It's working . . . sorta.")
