# Generated by Django 2.0.3 on 2020-04-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20200427_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceDefault',
            fields=[
                ('hostname', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
    ]
