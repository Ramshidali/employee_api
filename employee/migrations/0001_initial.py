# Generated by Django 3.2.13 on 2022-11-14 19:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Not an valid number', regex='^\\+?1?\\d{9,15}$')])),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('10', 'Male'), ('20', 'Female')], max_length=10)),
                ('hno', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='employee')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employee',
                'db_table': 'employee',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='WorkingExperiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=128)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('address', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedetails')),
            ],
            options={
                'verbose_name': 'Working Experience',
                'verbose_name_plural': 'Working Experience',
                'db_table': 'working_experience',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=128)),
                ('percentage', models.PositiveIntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedetails')),
            ],
            options={
                'verbose_name': 'qualifications',
                'verbose_name_plural': 'qualifications',
                'db_table': 'qualifications',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='project')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedetails')),
            ],
            options={
                'verbose_name': 'projects',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
                'ordering': ('-id',),
            },
        ),
    ]
