# Generated by Django 5.1.7 on 2025-04-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
    ]
