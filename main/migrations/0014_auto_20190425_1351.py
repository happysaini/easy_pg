# Generated by Django 2.1.3 on 2019-04-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190425_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgdetaildata',
            name='pic',
            field=models.ImageField(default='media/defaultpic.png', upload_to='easypg/main/static/media'),
        ),
    ]