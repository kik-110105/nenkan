# Generated by Django 4.2.6 on 2024-02-15 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eightch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toukou',
            name='description',
        ),
    ]
