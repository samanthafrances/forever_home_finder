# Generated by Django 5.0.4 on 2024-04-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_adoptioninquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.jpg', null=True, upload_to='avatars/'),
        ),
    ]
