from django.urls import path
from . import views

#Static urls
urlpatterns = [
    path('',views.home_view,name='home'),
    path('about',views.about_view,name='about'),
    path('contact',views.contact_view,name='contact'),
]