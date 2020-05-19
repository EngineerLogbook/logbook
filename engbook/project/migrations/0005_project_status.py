# Generated by Django 3.0.5 on 2020-05-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200517_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('ideation', 'ideation'), ('development', 'development'), ('testing', 'testing'), ('completed', 'completed')], max_length=11, null=True),
        ),
    ]
