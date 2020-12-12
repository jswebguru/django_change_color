# Generated by Django 2.2.12 on 2020-12-12 05:19

import blog.models
import colorfield.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=blog.models.upload_to_image)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'db_table': 'index',
            },
        ),
    ]
