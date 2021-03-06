# Generated by Django 3.2.8 on 2021-12-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20211214_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth_categor_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_categor', models.CharField(max_length=25, verbose_name='Код')),
                ('categor_price', models.CharField(max_length=25, verbose_name='Категория ткани')),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Категории тканей',
                'verbose_name_plural': 'Категория ткани',
            },
        ),
        migrations.RemoveField(
            model_name='cloth_items',
            name='categor_price',
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='description',
            field=models.TextField(blank=True, max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='image_link',
            field=models.URLField(blank=True, max_length=250, verbose_name='Ссылка на фото поставщика'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='name_item',
            field=models.CharField(max_length=250, verbose_name='Название ткани'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='purpose_item',
            field=models.TextField(blank=True, max_length=250, verbose_name='Предназначена для..'),
        ),
        migrations.AlterField(
            model_name='cloth_items',
            name='sale_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='cloth_items',
            name='categor_price',
            field=models.ManyToManyField(to='catalog.Cloth_categor_price'),
        ),
    ]
