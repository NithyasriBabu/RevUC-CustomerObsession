# Generated by Django 3.0.3 on 2020-02-23 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_households_transactions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='households',
            name='id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AlterField(
            model_name='households',
            name='hshd_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='hshd_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Households'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Products'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='trans_date',
            field=models.DateField(auto_now=True),
        ),
    ]
