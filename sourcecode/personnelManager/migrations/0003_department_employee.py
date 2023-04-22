# Generated by Django 4.2 on 2023-04-22 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnelManager', '0002_client_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_slug', models.SlugField(blank=True, unique=True)),
                ('department_name', models.CharField(blank=True, max_length=50)),
                ('department_description', models.CharField(blank=True, max_length=100)),
                ('department_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_slug', models.SlugField(blank=True, unique=True)),
                ('employeement_status', models.CharField(blank=True, choices=[('F', 'Full Time'), ('P', 'Part Time'), ('C', 'Casual')], max_length=1)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_id', to=settings.AUTH_USER_MODEL)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_id', to='personnelManager.department')),
            ],
        ),
    ]
