# Generated by Django 3.1.7 on 2021-03-13 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CostosCirugia', '0007_auto_20210313_0914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nombrecanasta',
            options={'ordering': ['name_can']},
        ),
        migrations.RenameField(
            model_name='nombrecanasta',
            old_name='nombre_canasta',
            new_name='name_can',
        ),
    ]
