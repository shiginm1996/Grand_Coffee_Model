# Generated by Django 4.2.5 on 2024-02-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0026_remove_place_order_prod_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_details',
            old_name='zip',
            new_name='pin',
        ),
        migrations.AddField(
            model_name='cart_details',
            name='prod_img',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart_details',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
