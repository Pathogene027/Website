# Generated by Django 4.0.4 on 2022-06-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_address_bio_doctor_product_delete_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='fname',
            new_name='Doc_fname',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='sname',
            new_name='Doc_sname',
        ),
        migrations.AlterField(
            model_name='people',
            name='fname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='sname',
            field=models.CharField(max_length=50),
        ),
    ]
