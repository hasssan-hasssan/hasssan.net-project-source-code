# Generated by Django 3.0.3 on 2021-02-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210206_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='teach',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teach',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
