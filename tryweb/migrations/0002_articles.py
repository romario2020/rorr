# Generated by Django 3.2.8 on 2021-10-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонсы')),
                ('full_text', models.TextField(verbose_name='Новость')),
                ('dates', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
