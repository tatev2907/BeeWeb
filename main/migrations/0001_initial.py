# Generated by Django 3.1.2 on 2020-10-22 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('shortURL', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('targetURL', models.CharField(max_length=2083)),
                ('countV', models.IntegerField(default=0)),
                ('SubUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]