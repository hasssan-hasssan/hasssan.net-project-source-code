# Generated by Django 3.0.3 on 2020-12-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201204_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_description', models.TextField()),
                ('body_description', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='blog.Post')),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]