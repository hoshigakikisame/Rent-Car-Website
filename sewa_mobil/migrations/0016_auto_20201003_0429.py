# Generated by Django 3.1.1 on 2020-10-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa_mobil', '0015_mobil_rata_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobil',
            name='rata_rating',
        ),
        migrations.AlterField(
            model_name='mobil',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
