# Generated by Django 2.2.6 on 2020-01-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20200108_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='works_since',
            field=models.CharField(blank=True, max_length=50, verbose_name='works since'),
        ),
    ]
