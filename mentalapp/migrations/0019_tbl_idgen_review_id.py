# Generated by Django 4.0.4 on 2022-08-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalapp', '0018_tbl_query_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_idgen',
            name='review_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
