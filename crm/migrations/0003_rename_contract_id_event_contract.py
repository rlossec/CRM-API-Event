# Generated by Django 3.2.5 on 2021-07-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210725_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='contract_id',
            new_name='contract',
        ),
    ]
