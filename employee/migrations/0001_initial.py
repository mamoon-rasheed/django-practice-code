# Generated by Django 5.0.3 on 2024-05-01 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.designation')),
                ('jobdescription', models.ManyToManyField(to='employee.jobdescription')),
            ],
        ),
    ]
