# Generated by Django 3.0.7 on 2020-06-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatserver', '0007_auto_20200620_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatid',
            name='chatter',
        ),
        migrations.AddField(
            model_name='chatid',
            name='chatter',
            field=models.ManyToManyField(null=True, to='chatserver.username'),
        ),
        migrations.RemoveField(
            model_name='chatid',
            name='roomname',
        ),
        migrations.AddField(
            model_name='chatid',
            name='roomname',
            field=models.ManyToManyField(null=True, to='chatserver.roomId'),
        ),
    ]