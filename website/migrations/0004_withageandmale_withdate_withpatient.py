# Generated by Django 5.0 on 2023-12-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_male_alter_room_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithAgeAndMale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=50)),
                ('data', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WithDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WithPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
            ],
        ),
    ]
