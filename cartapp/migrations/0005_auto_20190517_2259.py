# Generated by Django 2.2.1 on 2019-05-17 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0004_auto_20190512_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', related_query_name='cart', to='goodsapp.Book'),
        ),
        migrations.AlterField(
            model_name='bookincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', related_query_name='book', to='cartapp.Cart'),
        ),
    ]
