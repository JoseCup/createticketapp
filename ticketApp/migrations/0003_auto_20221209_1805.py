# Generated by Django 3.1 on 2022-12-10 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketApp', '0002_ticket_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, max_length=255, null=True)),
                ('msg_from', models.CharField(blank=True, max_length=255, null=True)),
                ('msg_to', models.CharField(blank=True, max_length=255, null=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.ticket')),
            ],
        ),
    ]