# Generated by Django 3.1.2 on 2023-04-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230418_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Tags'),
        ),
    ]
