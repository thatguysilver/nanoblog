from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContentForm
from .models import Post, List

def post(request ):
    #testvar = "TEST VARIABLE PLZ IGNORE"
    post_list = Post.objects.order_by('id')
    pub_date = Post.pub_date

    to_do_list = List.objects.order_by('id')
    to_do_date = List.pub_date
    
    return render(request, 'posts/main.html', {
            'post': post_list, 'pub_date' : pub_date,
            'to_do_list':to_do_list, 'to_do_date':to_do_date}, 
    )

def content_get(request):

    if request.method == 'POST':

        form = ContentForm(request.POST)

        return render(request, 'main.html', {'form':form})
