# Generated by Django 5.0.2 on 2024-02-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Electronics'), (2, 'Earphones'), (3, 'Speaker'), (4, 'Mobile')], verbose_name='Category'),
        ),
    ]
