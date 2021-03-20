# Generated by Django 3.1.7 on 2021-03-13 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CostosCirugia', '0005_auto_20210312_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ganancia', models.FloatField(default=0, verbose_name='Ganancia')),
                ('procedimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CostosCirugia.procedimiento', verbose_name='Nombre del Procedimiento')),
                ('tipoProcedimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CostosCirugia.tipoprocedimiento', verbose_name='Tipo Procedimiento')),
            ],
        ),
    ]
