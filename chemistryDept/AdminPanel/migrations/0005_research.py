# Generated by Django 4.0.4 on 2022-07-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0004_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_title', models.TextField(max_length=100)),
                ('research_cover', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('research_description', models.TextField(max_length=250)),
                ('project_include', models.TextField(max_length=250)),
                ('publication_video', models.TextField(max_length=100)),
                ('publication_details', models.TextField(max_length=250)),
            ],
        ),
    ]
