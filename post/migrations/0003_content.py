# Generated by Django 3.0.8 on 2020-08-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200816_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='media/test_img.jpg', upload_to='')),
            ],
        ),
    ]
