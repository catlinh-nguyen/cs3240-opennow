# Generated by Django 3.1.6 on 2021-04-12 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('open_now', '0003_auto_20210408_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[], default=5)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_now.business')),
            ],
        ),
    ]
