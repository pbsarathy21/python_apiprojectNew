# Generated by Django 2.1.7 on 2019-03-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0005_remove_task_my_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
