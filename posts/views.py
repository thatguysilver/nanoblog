from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post(request ):
    testvar = "TEST VARIABLE PLZ IGNORE"
    post = Post.objects.all()
    
    return render(request, 'posts/main.html',\
            {'post': post}, {'post':post}
    )
