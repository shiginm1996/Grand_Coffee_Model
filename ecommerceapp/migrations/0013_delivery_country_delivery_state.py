# Generated by Django 4.2.5 on 2023-09-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0012_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='state',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
