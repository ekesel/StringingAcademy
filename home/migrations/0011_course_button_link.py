# Generated by Django 4.1.6 on 2023-03-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='button_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
