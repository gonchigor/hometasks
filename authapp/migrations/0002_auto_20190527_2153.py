# Generated by Django 2.2.1 on 2019-05-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userext',
            name='dop_info',
            field=models.TextField(blank=True, null=True, verbose_name='дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='userext',
            name='home_adress1',
            field=models.TextField(blank=True, null=True, verbose_name='домашний адрес - адрес1'),
        ),
        migrations.AlterField(
            model_name='userext',
            name='home_adress2',
            field=models.TextField(blank=True, null=True, verbose_name='домашний адрес - адрес2'),
        ),
        migrations.AlterField(
            model_name='userext',
            name='home_city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='домашний адрес - город'),
        ),
        migrations.AlterField(
            model_name='userext',
            name='home_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='домашний адрес - страна'),
        ),
        migrations.AlterField(
            model_name='userext',
            name='home_index',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='домашний адрес - индекс'),
        ),
    ]
