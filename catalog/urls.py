from django.urls import path
from . import views

urlpatterns = [
    path('', views.categor, name='categor'),
    path('categor/', views.categor, name='categor'),
    path('categor/<slug:categor_name>/',
         views.categor_name, name='categor_name'),
    path('categor/<int:categor_id>/',
         views.categor_id, name='categor_id'),
    path('categor/cloths', views.cloths_items, name='cloths'),
    path('categor/models', views.models, name='models'),
    path('constrdemo', views.constrdemo, name='constrdemo'),
]
