# Generated by Django 2.2.1 on 2019-05-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensionsapp', '0009_auto_20190502_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agerestriction',
            options={'ordering': ['order'], 'verbose_name': 'возрастное ограничение', 'verbose_name_plural': 'возрастные ограничения'},
        ),
        migrations.AddField(
            model_name='agerestriction',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Номер в списке'),
            preserve_default=False,
        ),
    ]
