# Generated by Django 3.2.5 on 2022-06-08 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0008_auto_20220429_1212'),
        ('cliente', '0001_initial'),
        ('store', '0002_auto_20220416_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('detalhes', models.CharField(blank=True, max_length=255, null=True)),
                ('forma_pag', models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Débito'), ('3', 'Crédito'), ('4', 'PIX')], default='0', max_length=3)),
                ('obs', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente')),
                ('item', models.ManyToManyField(blank=True, null=True, to='item.Item')),
                ('loja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
