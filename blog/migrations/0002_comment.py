# Generated by Django 3.0.3 on 2020-12-01 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.BooleanField(default=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_comments', to='blog.Post')),
            ],
            options={
                'ordering': ['-create'],
            },
        ),
    ]
