# Generated by Django 2.2.28 on 2022-05-01 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):


    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ringapp', '0058_auto_20220501_1311')
    ]

    state_operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.SmallIntegerField(choices=[(0, 'ring'), (1, 'citation'), (2, 'theorem'), (3, 'other'), (4, 'property of a ring'), (5, 'property'), (6, 'feature')])),
                ('status', models.SmallIntegerField(choices=[(-2, 'need info'), (-1, 'declined'), (0, 'pending'), (1, 'accepted'), (2, 'withdrawn')], default=0)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('response', models.TextField(blank=True, max_length=200, null=True)),
                ('unread', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
