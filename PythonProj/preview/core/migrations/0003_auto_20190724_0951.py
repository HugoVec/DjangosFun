# Generated by Django 2.2.3 on 2019-07-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190718_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=90),
        ),
    ]
