# Generated by Django 3.0.3 on 2021-06-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='variant',
            new_name='product_id',
        ),
        migrations.AlterField(
            model_name='variant',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]