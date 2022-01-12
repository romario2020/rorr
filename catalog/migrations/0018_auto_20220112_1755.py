# Generated by Django 3.2.8 on 2022-01-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_model_group_photo_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth_group',
            name='main_photo',
            field=models.ImageField(blank=True, upload_to='cloth_group/', verbose_name='Ссылка фото'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='photo_item',
            field=models.ImageField(upload_to='cloth_items/', verbose_name='основное фото'),
        ),
    ]