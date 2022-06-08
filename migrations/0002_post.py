# Generated by Django 4.0.4 on 2022-06-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100000)),
                ('post_content', models.CharField(max_length=100000)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
