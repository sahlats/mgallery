# Generated by Django 5.1 on 2024-09-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('runtime', models.PositiveIntegerField()),
                ('directer', models.CharField(max_length=200)),
            ],
        ),
    ]
