# Generated by Django 3.1.2 on 2020-10-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='checked_by',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
