# Generated by Django 3.1.1 on 2020-10-02 21:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sewa_mobil', '0016_auto_20201003_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='ratinged_by',
            field=models.ManyToManyField(blank=True, related_name='rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
