# Generated by Django 3.1.7 on 2021-03-15 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CostosCirugia', '0008_auto_20210313_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canasta',
            name='conceptoCanasta',
        ),
        migrations.DeleteModel(
            name='ConceptoCanasta',
        ),
    ]
