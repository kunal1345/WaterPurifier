# Generated by Django 2.0.6 on 2019-07-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCharges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=225, null=True, unique=True)),
                ('price', models.CharField(default='', max_length=225, null=True)),
            ],
        ),
    ]
