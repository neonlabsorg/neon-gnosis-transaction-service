# Generated by Django 2.2.7 on 2019-11-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0003_auto_20191107_1459"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internaltx",
            name="error",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="internaltx",
            name="trace_address",
            field=models.CharField(max_length=600),
        ),
    ]
