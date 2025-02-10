# Generated by Django 5.1.6 on 2025-02-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('balance', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Waiting'), (2, 'Active'), (3, 'Left')], default=1)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'ordering': ['-id'],
            },
        ),
    ]
