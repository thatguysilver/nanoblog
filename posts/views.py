from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def post(request ):
    testvar = "TEST VARIABLE PLZ IGNORE"
    post = Post.objects.all()
    
    return render(request, 'posts/main.html',\
            {'testvar': testvar}, {'post':post}
    )
