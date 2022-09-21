# Generated by Django 4.1.1 on 2022-09-21 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, help_text='Descripcion de la app', max_length=1111, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='projects',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
