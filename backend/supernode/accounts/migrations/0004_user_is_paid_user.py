# Generated by Django 4.1.5 on 2024-02-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_paid_user',
            field=models.BooleanField(default=False),
        ),
    ]
