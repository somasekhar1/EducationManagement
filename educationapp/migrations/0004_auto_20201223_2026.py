# Generated by Django 3.1.4 on 2020-12-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationapp', '0003_studentadddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]