# Generated by Django 3.2.6 on 2021-08-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_remove_category_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='descricao',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
