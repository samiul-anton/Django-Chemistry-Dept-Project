# Generated by Django 4.0.4 on 2022-07-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourceApp', '0004_computing'),
    ]

    operations = [
        migrations.AddField(
            model_name='computing',
            name='computing_type',
            field=models.TextField(choices=[('Image', 'Image'), ('Video', 'Video')], default='Image'),
            preserve_default=False,
        ),
    ]
