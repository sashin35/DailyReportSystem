# Generated by Django 4.0.6 on 2022-09-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nippo', '0002_remove_dailyreportmodel_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreportmodel',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreportmodel',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
