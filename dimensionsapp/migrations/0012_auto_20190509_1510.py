# Generated by Django 2.2.1 on 2019-05-09 12:10

from django.db import migrations


def export_customer_company(apps, schema_editor):
    Author = apps.get_model('dimensionsapp', 'Author')
    for author in Author.objects.all():
        author.namePublic = author.name
        author.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dimensionsapp', '0011_author_namepublic'),
    ]

    operations = [
        migrations.RunPython(export_customer_company),
    ]
