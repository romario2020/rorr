from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('about', views.about, name='about'),
    path('biss', views.biss, name='biss'),
    path('frame', views.frame, name='frame'),

]
