# Generated by Django 4.0.4 on 2022-08-01 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentalapp', '0011_tbl_expert_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_article',
            fields=[
                ('article_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('uploaded_date', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=100)),
                ('expert_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentalapp.tbl_expert')),
            ],
            options={
                'db_table': 'tbl_article',
            },
        ),
    ]
