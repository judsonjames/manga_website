# Generated by Django 2.0.5 on 2018-08-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_remove_manga_manga_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='cover',
            field=models.CharField(default='', max_length=50),
        ),
    ]
