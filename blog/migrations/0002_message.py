# Generated by Django 2.0.2 on 2018-02-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('body', models.TextField(max_length=256)),
                ('created_time', models.DateTimeField()),
            ],
        ),
    ]
