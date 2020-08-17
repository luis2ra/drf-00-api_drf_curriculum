# Generated by Django 2.2.10 on 2020-08-16 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_education', to=settings.AUTH_USER_MODEL),
        ),
    ]
