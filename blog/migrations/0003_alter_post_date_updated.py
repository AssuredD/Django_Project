# Generated by Django 4.1 on 2022-08-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
