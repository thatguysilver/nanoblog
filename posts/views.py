from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post(request):
    testvar = "TEST VARIABLE PLZ IGNORE"
    return render(request, 'posts/main.html', {'testvar': testvar})
