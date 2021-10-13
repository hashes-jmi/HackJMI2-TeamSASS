# Generated by Django 3.1.7 on 2021-10-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthIDApp', '0007_auto_20211010_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_medical',
            name='blood_group',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='basic_medical',
            name='height',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='basic_medical',
            name='weight',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
