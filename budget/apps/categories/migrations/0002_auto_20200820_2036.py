# Generated by Django 3.0.8 on 2020-08-20 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="category", name="budget",),
        migrations.AddField(
            model_name="category",
            name="type",
            field=models.CharField(default="EXPENSE", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
