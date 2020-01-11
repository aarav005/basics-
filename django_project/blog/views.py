from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
#use as a dummy data ... 
'''posts=[
    {
        'author':'aarav',
        'title': 'blog post',
        'content':'first post',
        'date_posted':'october',
    },
    {'author':'jane',
        'title': 'blog post',
        'content':'second post',
        'date_posted':'october',
    }
]'''

def home(request): # the request is an attribut that has to be inside
    #return HttpResponse('<h1>blog section</h1>')
    
    #adding template 
    #making the template dynamic by adding context
    #context={'posts':posts,'title':'blogpost'} # passing the dummy data from above
    context={'posts':Post.objects.all(),'title':'blogpost'} # passing the database data 
    return render(request,"blog/home.html",context)# adding context lets us pass the data into the function
   
def about(request): # the url for this logic has to be set in blog url,,, it doesn't need to be maaped with the main project it is in blogs views
    return HttpResponse('<h1>blog-about</h1>')
