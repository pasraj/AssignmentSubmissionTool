# Generated by Django 3.2.9 on 2021-11-27 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0011_alter_subjectrequest_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectrequest',
            old_name='teacher',
            new_name='user',
        ),
    ]
