# Generated by Django 5.1.1 on 2024-11-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
