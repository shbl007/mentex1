# Generated by Django 4.0.4 on 2022-07-22 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addexpert',
            new_name='tbl_expert',
        ),
        migrations.AlterModelTable(
            name='tbl_expert',
            table='tbl_expert',
        ),
    ]
