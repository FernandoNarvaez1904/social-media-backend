# Generated by Django 4.0.3 on 2022-04-07 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]