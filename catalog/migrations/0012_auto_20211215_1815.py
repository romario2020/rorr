# Generated by Django 3.2.8 on 2021-12-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_cloth_items_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth_items',
            name='categor_price',
            field=models.ManyToManyField(blank=True, to='catalog.Cloth_categor_price'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='color_cloth',
            field=models.ManyToManyField(blank=True, to='catalog.Cloth_color'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='parent_category',
            field=models.ManyToManyField(blank=True, to='catalog.Cloth_group'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='photo_item',
            field=models.ImageField(blank=True, upload_to='media\\cloth_items', verbose_name='основное фото'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='vendor',
            field=models.ManyToManyField(blank=True, related_name='Поставщик', to='catalog.Vendor'),
        ),
    ]
