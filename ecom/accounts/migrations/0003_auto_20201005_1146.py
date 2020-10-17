# Generated by Django 3.1.2 on 2020-10-05 06:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201005_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproductmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addproductmodel',
            name='product_added_by',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addproductmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]