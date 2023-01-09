# Generated by Django 3.2.4 on 2023-01-07 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20230107_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='SAT',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(400), django.core.validators.MaxValueValidator(1600)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='UNWEIGHTED_GPA',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(4)]),
        ),
    ]
