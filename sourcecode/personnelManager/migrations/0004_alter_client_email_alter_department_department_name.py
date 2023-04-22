# Generated by Django 4.2 on 2023-04-22 06:28

from django.db import migrations, models
import personnelManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('personnelManager', '0003_department_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(blank=True, max_length=50, validators=[personnelManager.models.validate_only_letters]),
        ),
    ]
