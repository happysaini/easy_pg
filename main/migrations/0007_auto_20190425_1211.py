# Generated by Django 2.1.3 on 2019-04-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190425_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgdetaildata',
            name='pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
