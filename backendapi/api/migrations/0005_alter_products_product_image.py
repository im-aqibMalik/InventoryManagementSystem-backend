# Generated by Django 3.2.6 on 2021-08-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210826_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]