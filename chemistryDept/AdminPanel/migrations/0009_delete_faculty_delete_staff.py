# Generated by Django 4.0.4 on 2022-07-18 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0008_research_by_area_delete_research'),
    ]

    operations = [
        migrations.DeleteModel(
            name='faculty',
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
