# Generated by Django 3.2.8 on 2021-10-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
