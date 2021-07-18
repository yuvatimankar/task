# Generated by Django 3.2.4 on 2021-07-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ino', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='images')),
                ('letterdate', models.DateField(max_length=10)),
                ('recdate', models.DateField(max_length=10)),
                ('receivedbystaff', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('Remark', models.IntegerField(max_length=5)),
            ],
        ),
    ]
