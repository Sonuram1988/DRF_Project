# Generated by Django 4.1.7 on 2023-02-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default='Hello', max_length=10),
            preserve_default=False,
        ),
    ]
