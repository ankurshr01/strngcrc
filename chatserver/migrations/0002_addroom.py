# Generated by Django 3.0.7 on 2020-06-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnumber', models.TextField()),
            ],
        ),
    ]
