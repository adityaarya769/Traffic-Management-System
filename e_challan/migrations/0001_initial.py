# Generated by Django 3.1.1 on 2020-09-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Number', models.CharField(max_length=100)),
                ('Challan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Number', models.CharField(max_length=100)),
                ('Challan', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
            ],
        ),
    ]
