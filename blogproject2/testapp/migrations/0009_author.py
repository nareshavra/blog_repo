# Generated by Django 3.2.7 on 2021-10-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20211017_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]
