# Generated by Django 5.1.5 on 2025-01-31 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Counselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('given_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=10)),
                ('born_date', models.DateField()),
                ('born_place', models.CharField(max_length=255)),
                ('born_country', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('position', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('division', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_address', models.EmailField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminUser.category')),
                ('gmail_addresses', models.ManyToManyField(blank=True, to='adminUser.gmail')),
                ('images', models.ManyToManyField(blank=True, to='adminUser.image')),
                ('phone_numbers', models.ManyToManyField(blank=True, to='adminUser.phone')),
            ],
        ),
    ]
