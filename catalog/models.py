from django.db import models
from django.utils.translation import gettext as _
import xml.etree.ElementTree as ET
import os
from django.urls import reverse


class Cloth_color(models.Model):
    code_color = models.CharField('Код', blank=True, max_length=25)
    color_main = models.CharField('Основной цвет', max_length=25)
    color_hex = models.CharField('HEX', max_length=10, blank=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.color_main

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Каталог цветов'
        verbose_name_plural = 'Цвет'
        ordering = ['color_main']


class Vendor(models.Model):
    code_vendor = models.CharField('Код', max_length=25)
    name_vendor = models.CharField('Поставщик', max_length=50)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name_vendor

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Поставщика'
        verbose_name_plural = 'Поставщики'
        ordering = ['name_vendor']


class Cloth_categor_price(models.Model):
    code_categor = models.CharField('Код', max_length=25)
    categor_price = models.CharField('Категория ткани', max_length=25)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.categor_price

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Категории тканей'
        verbose_name_plural = 'Категория ткани'
        ordering = ['categor_price']

# Create cloth_group


class Cloth_group(models.Model):
    code_group = models.CharField('Код группы', max_length=25, blank=True)
    name_group = models.CharField('Тип ткани', max_length=250)
    purpose_group = models.TextField('Назначение', max_length=250, blank=True)
    anons_group = models.CharField('Анонс', max_length=100, blank=True)
    dates = models.DateField('Дата создания', auto_now=True)
    url_group = models.URLField('Адрес группы', max_length=200, blank=True)
    main_photo = models.ImageField('Ссылка фото', upload_to='cloth_group/',
                                   height_field=None, width_field=None,
                                   max_length=100, blank=True)

    def __str__(self):
        return self.name_group

    # что бы в админк'е показывались без ss на конце
    class Meta:
        verbose_name = 'Группы тканей'
        verbose_name_plural = 'Группа ткани'
        ordering = ['name_group']


# model sofa group диван прямой
class Cloth_items(models.Model):
    code_item = models.CharField('Код', max_length=25, unique=True)
    name_item = models.CharField('Название ткани', max_length=250)
    photo_item = models.ImageField(
        'основное фото', upload_to='cloth_items/')
    vendor = models.ManyToManyField(Vendor, 'Поставщик', blank=True)
    color_cloth = models.ManyToManyField(Cloth_color, blank=True)
    parent_category = models.ManyToManyField(Cloth_group, blank=True)
    categor_price = models.ManyToManyField(
        Cloth_categor_price, default=0, blank=True)
    sale_price = models.PositiveIntegerField('Стоимость', default=0)
    image_link = models.URLField(
        'Ссылка на фото поставщика', max_length=250, blank=True)
    description = models.TextField('Описание', max_length=250, blank=True)
    purpose_item = models.TextField(
        'Предназначена для..', max_length=250, blank=True)
    time_create = models.DateTimeField()
    time_update = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name_item

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Ткань'
        verbose_name_plural = 'Ткани'
        ordering = ['-id']


# model sofa group диван прямой
class Model_group(models.Model):
    code_group = models.CharField('Код группы', max_length=25)
    name_group = models.CharField('Тип дивана', max_length=250)
    purpose_group = models.TextField(
        'Назначение, для..', max_length=250, blank=True)
    photo_group = models.ImageField(upload_to='type_model/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name_group

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Модели диванов'
        verbose_name_plural = 'Модель диванов'
        ordering = ['name_group']


# парсер товаров по фиду с азбуки
class Azbuka_items(models.Model):
    id_item = models.CharField('Код товара', max_length=25)
    title = models.CharField('title', max_length=250)
    availability = models.CharField(
        'availability', max_length=25)
    condition = models.CharField('condition', max_length=25)
    product_category = models.CharField(
        'product_category', max_length=35)
    parent_product_category = models.CharField(
        'parent_product_category', max_length=35)
    price = models.CharField('price', max_length=25)
    sale_price = models.CharField('sale_price', max_length=25)
    image_link = models.URLField('image_link', max_length=250)
    description = models.TextField('description', max_length=250, blank=True)

    def __str__(self):
        return self.title

    # что бы в админке показывались без ss на конце

    class Meta:
        verbose_name = 'Товары Азбуки'
        verbose_name_plural = 'Товар Азбуки'
        ordering = ['title', 'id']
