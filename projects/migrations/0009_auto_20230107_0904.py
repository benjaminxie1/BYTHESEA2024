# Generated by Django 3.2.4 on 2023-01-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20230107_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='sat_act',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uwgpa',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='wgpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]