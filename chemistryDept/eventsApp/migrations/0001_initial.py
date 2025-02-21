# Generated by Django 4.0.4 on 2022-08-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seminer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seminer_title', models.CharField(max_length=200)),
                ('seminer_description', models.TextField(max_length=500)),
                ('seminer_details', models.TextField(max_length=500)),
                ('seminer_speakers', models.CharField(max_length=500)),
                ('seminer_datetime', models.DateTimeField()),
                ('seminer_location', models.CharField(max_length=200)),
                ('seminar_cover', models.ImageField(blank=True, null=True, upload_to='Images/')),
            ],
        ),
    ]
