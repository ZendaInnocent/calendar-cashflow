# Generated by Django 3.0.8 on 2020-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('payment_type', models.CharField(choices=[('CH', 'Check'), ('CA', 'Cash'), ('PA', 'Payment')], max_length=2)),
                ('account', models.CharField(choices=[('BOZ', 'Bank Of Fredders'), ('BI', 'Building & Construction'), ('C', 'Cash'), ('CA', 'Checking Account'), ('EQ', 'Equipments'), ('IP', 'Insurance Paid'), ('LAM', 'Less Accum. Depreciation'), ('PC', 'Petty Cash'), ('SU', 'Supplies')], max_length=3)),
                ('status', models.CharField(choices=[('D', 'Deposit'), ('W', 'Withdrawal')], max_length=2)),
                ('date', models.DateField()),
                ('starting_amount', models.FloatField(default=0)),
                ('ending_amount', models.FloatField(default=0)),
            ],
        ),
    ]
