# Generated by Django 3.2.6 on 2021-08-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
