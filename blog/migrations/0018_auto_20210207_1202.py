# Generated by Django 3.0.3 on 2021-02-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210207_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teach',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
