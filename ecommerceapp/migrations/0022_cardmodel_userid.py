# Generated by Django 4.2.5 on 2024-02-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0021_cardmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardmodel',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
