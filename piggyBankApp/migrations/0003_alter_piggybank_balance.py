# Generated by Django 4.2.6 on 2023-10-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggyBankApp', '0002_alter_goal_amount_alter_goal_goalname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piggybank',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]