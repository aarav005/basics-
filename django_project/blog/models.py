from django.db import models
from django.utils import timezone  
from django.contrib.auth.models import User #importing the user # one to many relation 

class Post(models.Model):
    # creating user profile to add post in the blog app
    title = models.CharField(max_length=100) # the max length of 100 characters
    content= models.TextField(default="")
    #auto_now =true updates the time when it was updated, # auto_now_add: sets the time when it was created 
    date_posted=models.DateTimeField(default=timezone.now) # default allows to change the time when needed.# notice now is not called yet but just passed
    author= models.ForeignKey(User,on_delete=models.CASCADE) # on_deletes deletes the user post when the user is deleted

    def __str__(self): # dunder method to display discriptive content of post while in shell
        return self.title

