# Generated by Django 2.1.4 on 2018-12-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooo', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='end_element',
            field=models.BooleanField(default=False, verbose_name='конечный элемент'),
        ),
    ]
