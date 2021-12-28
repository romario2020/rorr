from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонсы', max_length=250)
    full_text = models.TextField('Новость')
    dates = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    # что бы в админке показывались без ss на конце
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return f'/news/{self.id}'
