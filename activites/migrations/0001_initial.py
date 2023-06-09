# Generated by Django 4.2.2 on 2023-06-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(help_text='Store Event Details', max_length=150)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('event_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
