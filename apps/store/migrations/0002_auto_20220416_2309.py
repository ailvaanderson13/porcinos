# Generated by Django 3.2.5 on 2022-04-17 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
        migrations.AddField(
            model_name='store',
            name='id_store',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
