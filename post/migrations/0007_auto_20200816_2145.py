# Generated by Django 3.0.8 on 2020-08-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(default='test_img.jpg', upload_to=''),
        ),
    ]
