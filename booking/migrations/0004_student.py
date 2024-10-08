# Generated by Django 5.0.7 on 2024-07-10 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_course_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoiceno', models.TextField(max_length=40)),
                ('Name', models.TextField(max_length=40)),
                ('Batchtime', models.TimeField()),
                ('BSD', models.DateField()),
                ('phone1', models.TextField(max_length=50)),
                ('phone2', models.TextField(max_length=50)),
                ('Place', models.TextField(max_length=50)),
                ('BED', models.DateField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
                ('Course_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.course')),
            ],
        ),
    ]
