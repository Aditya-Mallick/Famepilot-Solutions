# Generated by Django 4.0.3 on 2022-04-05 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_customuser_name_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]