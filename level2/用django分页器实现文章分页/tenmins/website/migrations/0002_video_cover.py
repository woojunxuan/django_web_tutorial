# Generated by Django 2.0 on 2018-01-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover',
            field=models.FileField(null=True, upload_to='cover_image'),
        ),
    ]
