# Generated by Django 3.1.7 on 2021-03-26 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displayapis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.TextField(blank=True)),
            ],
        ),
    ]
