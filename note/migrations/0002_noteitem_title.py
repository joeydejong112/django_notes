# Generated by Django 2.2.10 on 2020-04-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteitem',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]
