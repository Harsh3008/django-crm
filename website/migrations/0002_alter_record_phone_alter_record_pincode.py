# Generated by Django 4.2.1 on 2023-06-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='pincode',
            field=models.CharField(max_length=20),
        ),
    ]
