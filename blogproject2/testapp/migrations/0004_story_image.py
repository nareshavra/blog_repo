# Generated by Django 3.2.7 on 2021-10-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_story_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
    ]
