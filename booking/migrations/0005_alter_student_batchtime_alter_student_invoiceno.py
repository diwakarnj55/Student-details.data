# Generated by Django 5.0.7 on 2024-07-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Batchtime',
            field=models.CharField(choices=[('09', '09.00 to 10.30'), ('1030', '10.30 to 12.00'), ('12', '12.00 to 01.30'), ('02', '02.00 to 03.30'), ('330', '03.30 to 05.00'), ('saturday', 'Saturday')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='Invoiceno',
            field=models.TextField(max_length=5),
        ),
    ]
