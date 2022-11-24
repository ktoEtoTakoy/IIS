# Generated by Django 4.1.2 on 2022-11-23 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0003_alter_walk_options_alter_walk_walker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='created', max_length=14)),
                ('task_start', models.DateTimeField(default=None, null=True)),
                ('task_end', models.DateTimeField(default=None, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.animal')),
                ('vet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-task_start',),
            },
        ),
    ]