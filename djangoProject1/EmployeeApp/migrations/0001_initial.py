# Generated by Django 4.1 on 2023-03-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("emp_id", models.IntegerField(primary_key=True, serialize=False)),
                ("emp_name", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=1)),
                ("marital_status", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=20)),
                ("position", models.CharField(max_length=20)),
                ("employment_status", models.CharField(max_length=25)),
                ("manager_name", models.CharField(max_length=30)),
                ("performance_score", models.CharField(max_length=20)),
                ("absences", models.IntegerField()),
                ("salary", models.FloatField()),
            ],
        ),
    ]
