# Generated by Django 4.1.7 on 2023-02-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
