# Generated by Django 3.2.9 on 2021-11-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.JSONField(default=dict),
        ),
    ]
