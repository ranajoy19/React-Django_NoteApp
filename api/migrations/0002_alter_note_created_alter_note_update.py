# Generated by Django 4.0 on 2021-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]