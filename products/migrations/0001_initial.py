# Generated by Django 3.0.3 on 2021-06-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=500)),
                ('handle', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_var', to='products.Product')),
            ],
        ),
    ]