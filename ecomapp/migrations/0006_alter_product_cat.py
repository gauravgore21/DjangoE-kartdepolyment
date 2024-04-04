# Generated by Django 5.0.2 on 2024-02-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Earphones'), (2, 'Speaker'), (3, 'Mobile'), (4, 'Camera'), (5, 'Headset'), (6, 'Watch'), (7, 'Power Bank')], verbose_name='Category'),
        ),
    ]
