# Generated by Django 2.2 on 2022-11-10 18:57

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('company', models.CharField(max_length=255)),
                ('client_date', models.DateField(auto_now_add=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('website', models.URLField(max_length=100)),
                ('budget', models.CharField(max_length=12)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='createquote.Client')),
            ],
        ),
    ]
