# Generated by Django 3.2.18 on 2023-03-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_club_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='country',
            field=models.CharField(default='undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='club',
            name='school',
            field=models.CharField(default='undefined', max_length=50),
        ),
    ]