# Generated by Django 5.0.4 on 2024-04-24 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_merge_20240424_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.blog'),
        ),
    ]