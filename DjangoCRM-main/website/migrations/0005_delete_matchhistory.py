# Generated by Django 5.0.1 on 2024-02-08 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MatchHistory',
        ),
    ]
