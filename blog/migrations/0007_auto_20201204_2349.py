# Generated by Django 3.0.3 on 2020-12-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=250, unique_for_date='publish'),
        ),
    ]
