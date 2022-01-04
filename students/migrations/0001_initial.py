# Generated by Django 4.0 on 2021-12-31 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('student_class', models.PositiveIntegerField()),
            ],
        ),
    ]