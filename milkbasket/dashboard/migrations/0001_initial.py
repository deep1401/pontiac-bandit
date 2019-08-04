# Generated by Django 2.2.4 on 2019-08-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BPM',
            fields=[
                ('customer_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('r1', models.CharField(max_length=20)),
                ('r2', models.CharField(max_length=20)),
                ('r3', models.CharField(max_length=20)),
                ('r4', models.CharField(max_length=20)),
                ('r5', models.CharField(max_length=20)),
                ('r6', models.CharField(max_length=20)),
                ('r7', models.CharField(max_length=20)),
                ('r8', models.CharField(max_length=20)),
                ('r9', models.CharField(max_length=20)),
                ('r10', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CP',
            fields=[
                ('customer_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('Sub_flag', models.IntegerField()),
                ('subscription', models.BooleanField()),
                ('Recency_flag', models.IntegerField()),
                ('Refreq', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RFM',
            fields=[
                ('customer_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('Recency_flag', models.IntegerField()),
                ('Freq_flag', models.IntegerField()),
                ('monetary_flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RO',
            fields=[
                ('customer_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('Recency_flag', models.IntegerField()),
                ('monetary_flag', models.IntegerField()),
            ],
        ),
    ]
