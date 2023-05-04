# Generated by Django 4.1.2 on 2023-05-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('prezime', models.CharField(max_length=100)),
                ('drzava', models.CharField(max_length=100)),
                ('subjekt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StartingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
