# Generated by Django 4.2.5 on 2023-09-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_itemup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemup',
            name='pimage',
            field=models.FileField(upload_to='ecommerceapp/static'),
        ),
    ]