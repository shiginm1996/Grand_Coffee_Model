# Generated by Django 4.2.5 on 2024-02-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0020_alter_cart_details_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=50)),
                ('cardno', models.CharField(max_length=50)),
                ('expiry', models.CharField(max_length=50)),
                ('cvv', models.CharField(max_length=50)),
            ],
        ),
    ]
