# Generated by Django 3.2.5 on 2022-04-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220424_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]