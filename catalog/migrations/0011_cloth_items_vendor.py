# Generated by Django 3.2.8 on 2021-12-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20211214_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth_items',
            name='vendor',
            field=models.ManyToManyField(related_name='Поставщик', to='catalog.Vendor'),
        ),
    ]
