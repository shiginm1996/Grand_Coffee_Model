# Generated by Django 4.2.5 on 2024-02-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0018_remove_delivery_lname_alter_delivery_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]
