# Generated by Django 4.0.4 on 2022-08-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchApp', '0005_research_overview_delete_research_by_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='research_by_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_fields', models.TextField(choices=[('Chemistry', 'Chemistry'), ('Chemical Engineering', 'Chemical Engineering'), ('Biomedical Engineering', 'Biomedical Engineering')])),
                ('research_title', models.CharField(max_length=250)),
                ('research_cover', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('research_description', models.TextField(max_length=250)),
                ('project_include', models.TextField(max_length=250)),
                ('publication_video', models.CharField(max_length=250)),
                ('publication_details', models.TextField(max_length=250)),
            ],
        ),
    ]
