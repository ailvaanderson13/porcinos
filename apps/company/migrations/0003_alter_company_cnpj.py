# Generated by Django 3.2.5 on 2022-04-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
