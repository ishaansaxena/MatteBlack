# Generated by Django 2.0.4 on 2018-07-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbols', '0004_auto_20180712_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='trackers',
            field=models.ManyToManyField(blank=True, default=None, to='investor.Investor'),
        ),
    ]
