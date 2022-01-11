from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from .models import *

# Create your views here.


menu_cloths = ['Индивидуальные', 'Мебельные']
menu_models = ['Прямые', 'Уголовой левый', 'Угловой правый']


def categor(request):
    return render(request, 'catalog/categor.html')


# def categor_name(request, categor_name):
#     # if (request.GET):
#     #     print(request.GET)  # отлавливаем гет запрос если он есть в строке
#     return render(request, 'catalog/categor.html')


# def categor_id(request, cat_id):
#     return render(request, 'catalog/categor.html')


def cloths(request):
    posts_cloths = Cloth_group.objects.all()
    return render(request, 'catalog/cloths.html',
                  {'posts_cloths': posts_cloths,
                   'menu_cloths': menu_cloths,
                   'title': "Каталог тканей"})


def cloths_items(request):
    posts_cloths_items = Cloth_items.objects.all()
    posts_cloths = Cloth_group.objects.all()
    return render(request, 'catalog/cloths.html',
                  {'posts_cloths_items': posts_cloths_items,
                   'posts_cloths': posts_cloths,
                   'title': "Каталог тканей"})


def models(request):
    posts = Model_group.objects.all()
    items_all = Azbuka_items.objects.all().order_by('title')
    items_sofa = Azbuka_items.objects.filter(
        parent_product_category='Мягкая мебель',
        product_category='Диваны прямые').order_by('title')
    return render(request, 'catalog/models.html',
                  {'posts': posts,
                   'title': 'Каталог моделей диванов',
                   'items_all': items_all,
                   'items_sofa': items_sofa
                   })


def constrdemo(request):
    posts_cloths_items = Cloth_items.objects.all()
    posts_cloths_items1 = Cloth_items.objects.filter(parent_category=1)
    posts_cloths_items2 = Cloth_items.objects.filter(parent_category=2)
    posts_cloths_items5 = Cloth_items.objects.filter(parent_category=5)
    posts_cloths_items6 = Cloth_items.objects.filter(parent_category=6)
    posts_cloth_group = Cloth_group.objects.all()
    return render(request, 'catalog/index_php.html',
                  {'posts_cloths_items': posts_cloths_items,
                   'posts_cloths_items1': posts_cloths_items1,
                   'posts_cloths_items2': posts_cloths_items2,
                   'posts_cloths_items5': posts_cloths_items5,
                   'posts_cloths_items6': posts_cloths_items6,
                   'posts_cloth_group': posts_cloth_group,
                   })
