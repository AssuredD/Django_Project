# Generated by Django 4.1 on 2022-08-26 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updated',
        ),
    ]
