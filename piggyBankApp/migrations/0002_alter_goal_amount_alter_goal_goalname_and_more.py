# Generated by Django 4.2.6 on 2023-10-27 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggyBankApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goalName',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='item',
            field=models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='piggybank',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='piggybank',
            name='starting_balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
