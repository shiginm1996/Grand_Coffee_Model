# Generated by Django 4.2.5 on 2023-10-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0015_alter_delivery_country_alter_delivery_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirmmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('address', models.CharField(max_length=400)),
                ('prodimg', models.FileField(upload_to='')),
                ('prod_details', models.CharField(max_length=400)),
                ('totalprice', models.IntegerField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('estimated_date', models.DateField()),
            ],
        ),
    ]
