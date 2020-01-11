from django.shortcuts import render,redirect
from django.contrib.auth.forms  import UserCreationForm
#lets aslo display some kind of messages...these are one time alert
from django.contrib import messages

# Cuser creation
def register(request):
    #working with the post data,,if we get post request it gets passes to form if not the empty post is passes
    if request.method=='POST':
        form=form = UserCreationForm(request.POST)
        #to validate the post,,if we are getting the fields and data that we expect
        if form.is_valid():
            form.save()# this saves the user 
            username=form.cleaned_data.get('username')
            messages.sucess(request,f'account created for{username}!')
            #redirecting
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    #rendering a template using this form...
    return render(request,'users/register.html',{'form':form})
