# Generated by Django 4.0.4 on 2022-08-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminer',
            name='featured',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
