# Generated by Django 2.1.3 on 2019-04-22 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_signupowndata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupowndata',
            old_name='owner_contact',
            new_name='ownercontact',
        ),
        migrations.RenameField(
            model_name='signupowndata',
            old_name='owner_email',
            new_name='owneremail',
        ),
        migrations.RenameField(
            model_name='signupowndata',
            old_name='owner_name',
            new_name='ownername',
        ),
        migrations.RenameField(
            model_name='signupowndata',
            old_name='owner_password',
            new_name='ownerpassword',
        ),
    ]
