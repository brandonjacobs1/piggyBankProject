# Generated by Django 4.2.6 on 2023-10-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggyBankApp', '0004_alter_piggybank_balance_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='accomplished',
            field=models.BooleanField(default=False),
        ),
    ]
