# Generated by Django 2.0.4 on 2018-07-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('symbol', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
