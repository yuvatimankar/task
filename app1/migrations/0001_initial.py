# Generated by Django 3.2.4 on 2021-06-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]
