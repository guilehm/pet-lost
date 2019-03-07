# Generated by Django 2.1.7 on 2019-03-07 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0002_auto_20190306_0008'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('situation', models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], max_length=128)),
                ('message', models.TextField()),
                ('rescued', models.BooleanField(default=False)),
                ('rescued_date', models.DateField(blank=True, null=True)),
                ('last_seen_district', models.CharField(max_length=512)),
                ('last_seen_detail', models.CharField(max_length=512)),
                ('lost_date', models.DateField(blank=True, db_index=True, null=True)),
                ('found_date', models.DateField(blank=True, db_index=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('last_seen_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='location.City')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='pet.Pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
