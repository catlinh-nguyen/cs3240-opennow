# Generated by Django 3.2 on 2021-05-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_now', '0011_auto_20210504_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.CharField(default='Guest', max_length=200),
        ),
    ]
