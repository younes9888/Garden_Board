# Generated by Django 3.2.16 on 2022-10-13 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_alter_garden_tips_tips_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden_tips',
            name='tips_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 10, 13, 11, 12, 5, 117609)),
        ),
    ]
