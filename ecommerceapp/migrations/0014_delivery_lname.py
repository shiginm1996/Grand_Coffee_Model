# Generated by Django 4.2.5 on 2023-09-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0013_delivery_country_delivery_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='lname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
