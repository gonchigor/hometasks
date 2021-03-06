# Generated by Django 2.2 on 2019-04-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensionsapp', '0005_author_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Возрастное ограничение',
                'verbose_name_plural': 'Возрастные ограничения',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
