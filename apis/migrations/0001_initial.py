# Generated by Django 3.0.3 on 2020-02-23 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('department', models.CharField(max_length=10)),
                ('commodity', models.CharField(max_length=25)),
                ('brand_type', models.CharField(max_length=10)),
                ('organic', models.BooleanField()),
            ],
        ),
    ]
