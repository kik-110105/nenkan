# Generated by Django 4.2.6 on 2024-02-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eightch', '0004_alter_toukou_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toukou',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
