from django.urls import path
from . import views # imports views from the current directory
urlpatterns=[
    path('',views.home,name='blog-home'), #'' sets this path as the home page, views.home is the functio we created in this directory blog
    path('about',views.about,name='blog-about'), # access this on webbrower through /blog/about
]