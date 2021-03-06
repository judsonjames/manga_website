# Generated by Django 2.1.5 on 2019-01-31 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0004_auto_20190130_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.ManyToManyField(to='navigation.Author'),
        ),
    ]
