# Generated by Django 2.2.4 on 2019-08-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20190804_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='RFM',
            fields=[
                ('customer_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('Recency_flag', models.IntegerField()),
                ('Freq_flag', models.IntegerField()),
                ('monetary_flag', models.IntegerField()),
            ],
        ),
    ]
