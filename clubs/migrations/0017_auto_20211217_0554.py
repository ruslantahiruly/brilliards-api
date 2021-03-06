# Generated by Django 2.2.6 on 2021-12-17 05:54

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0016_auto_20211006_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='is_medical_masks',
            field=models.BooleanField(default=False, verbose_name='вход только в медицинских масках'),
        ),
        migrations.AddField(
            model_name='club',
            name='is_pre_entry',
            field=models.BooleanField(default=False, verbose_name='entrance by appointment'),
        ),
        migrations.AddField(
            model_name='club',
            name='time_zone',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='time zone'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='customer_categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AL', 'Всем'), ('RT', 'Пенсионерам'), ('PP', 'Школьникам'), ('ST', 'Студентам'), ('BD', 'Именинникам'), ('RC', 'Постоянным клиентам')], default='AL', max_length=20, verbose_name='customer categories'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='days_of_the_week',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MO', 'Понедельник'), ('TU', 'Вторник'), ('WE', 'Среда'), ('TH', 'Четверг'), ('FR', 'Пятница'), ('SA', 'Суббота'), ('SU', 'Воскресенье')], max_length=20, verbose_name='days of the week'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='type',
            field=models.CharField(choices=[('DC', 'Скидка'), ('CR', 'Подарочный сертификат'), ('OT', 'Остальные')], default='DC', max_length=5, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='name',
            field=models.CharField(choices=[('VK', 'Вконтакте'), ('OK', 'Одноклассники'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('TM', 'Telegram'), ('IN', 'Instagram'), ('UT', 'YouTube'), ('TT', 'Tiktok')], max_length=5, verbose_name='name'),
        ),
    ]
