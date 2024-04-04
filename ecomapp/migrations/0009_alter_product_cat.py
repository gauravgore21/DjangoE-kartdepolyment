# Generated by Django 5.0.2 on 2024-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Earphones'), (2, 'Speaker'), (3, 'Mobile'), (4, 'Camera'), (5, 'Headset'), (6, 'Watch'), (7, 'Power Bank'), (8, 'Television'), (9, 'Laptop'), (10, 'Washing Machine')], verbose_name='Category'),
        ),
    ]
