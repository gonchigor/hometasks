# Generated by Django 2.2.4 on 2019-08-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curratesapp', '0002_auto_20190828_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currates',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Курс доллара'),
        ),
    ]
