# Generated by Django 3.2.7 on 2021-11-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeId', models.AutoField(primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=220)),
                ('department', models.CharField(max_length=220)),
                ('dateOfJoining', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuId', models.AutoField(primary_key=True, serialize=False)),
                ('restaurantId', models.IntegerField(verbose_name=11)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('summery', models.CharField(max_length=200)),
                ('price', models.FloatField(verbose_name=11)),
                ('createdOn', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('restaurantId', models.AutoField(primary_key=True, serialize=False)),
                ('restaurantName', models.CharField(max_length=220)),
                ('ownerName', models.CharField(max_length=220)),
                ('createdOn', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('voteId', models.AutoField(primary_key=True, serialize=False)),
                ('employeeId', models.IntegerField(verbose_name=11)),
                ('menuId', models.IntegerField(verbose_name=11)),
                ('votedOn', models.DateField()),
            ],
        ),
    ]
