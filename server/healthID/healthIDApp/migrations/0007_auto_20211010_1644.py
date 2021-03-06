# Generated by Django 3.1.7 on 2021-10-10 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthIDApp', '0006_allergies_belong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_medical',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='basic_medical',
            name='surgery',
        ),
        migrations.AddField(
            model_name='disease',
            name='belong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='healthIDApp.basic_medical'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='belong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='healthIDApp.basic_medical'),
        ),
    ]
