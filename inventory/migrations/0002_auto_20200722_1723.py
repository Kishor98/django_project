# Generated by Django 3.0.8 on 2020-07-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='type',
            field=models.CharField(choices=[('Frames', 'frames'), ('Other', 'other')], max_length=50),
        ),
    ]
