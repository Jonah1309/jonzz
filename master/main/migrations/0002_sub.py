# Generated by Django 3.1 on 2020-08-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=200)),
                ('sub_cat_name', models.CharField(max_length=200)),
            ],
        ),
    ]
