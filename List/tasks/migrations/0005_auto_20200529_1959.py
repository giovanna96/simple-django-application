# Generated by Django 3.0.6 on 2020-05-29 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200529_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-deadline', '-created_date')},
        ),
    ]
