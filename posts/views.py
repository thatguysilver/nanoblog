from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContentForm
from .models import Post

def post(request ):
    #testvar = "TEST VARIABLE PLZ IGNORE"
    post_list = Post.objects.order_by('id')
    pub_date = Post.pub_date
    
    return render(request, 'posts/main.html',
            {'post': post_list, 'pub_date' : pub_date}, 
    )

def content_get(request):

    if request.method == 'POST':

        form = ContentForm(request.POST)

        return render(request, 'main.html', {'form':form})
