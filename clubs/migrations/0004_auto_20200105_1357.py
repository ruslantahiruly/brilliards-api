# Generated by Django 2.2.6 on 2020-01-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_table_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='size',
            field=models.CharField(choices=[(12, '12 футов'), (11, '11 футов'), (10, '10 футов'), (9, '9 футов'), (8, '8 футов')], max_length=5, verbose_name='size'),
        ),
    ]
