# Generated by Django 4.0.4 on 2022-06-08 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenship', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('GPS_post_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_manu_date', models.DateField()),
                ('product_exp_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RemoveField(
            model_name='people',
            name='fn',
        ),
        migrations.RemoveField(
            model_name='people',
            name='sn',
        ),
        migrations.AddField(
            model_name='people',
            name='fname',
            field=models.CharField(default='John', max_length=50),
        ),
        migrations.AddField(
            model_name='people',
            name='sname',
            field=models.CharField(default='Doe', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='people',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.people'),
        ),
        migrations.AddField(
            model_name='bio',
            name='people',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.people'),
        ),
        migrations.AddField(
            model_name='address',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.people'),
        ),
    ]