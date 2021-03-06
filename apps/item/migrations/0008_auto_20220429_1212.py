# Generated by Django 3.2.5 on 2022-04-29 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_cnpj'),
        ('item', '0007_auto_20220418_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='loja',
        ),
        migrations.AddField(
            model_name='item',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
        migrations.AddField(
            model_name='item',
            name='empty',
            field=models.BooleanField(default=False),
        ),
    ]
