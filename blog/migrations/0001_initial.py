# Generated by Django 3.0.6 on 2020-05-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.TextField()),
                ('time', models.TextField()),
                ('choice', models.CharField(default='1', max_length=100, verbose_name='제휴카드')),
            ],
        ),
    ]