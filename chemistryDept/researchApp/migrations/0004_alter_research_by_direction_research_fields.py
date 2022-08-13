from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchApp', '0003_research_by_direction_research_cover_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research_by_direction',
            name='research_fields',
            field=models.TextField(choices=[('Sustainability Energy', 'Sustainability Energy'), ('Medical', 'Medical')]),
        ),
    ]
