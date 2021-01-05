# Generated by Django 3.0.8 on 2020-09-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0003_poster_description_full'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='sku',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
