# Generated by Django 5.0.1 on 2024-01-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=75)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, upload_to='')),
                ('link', models.URLField(blank=True, max_length=180)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updates', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
