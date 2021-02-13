# Generated by Django 2.2.6 on 2021-02-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=20)),
                ('tz', models.CharField(max_length=30)),
                ('period', models.ManyToManyField(to='throttletestapp.Period')),
            ],
        ),
    ]
