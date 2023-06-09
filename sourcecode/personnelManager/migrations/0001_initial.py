# Generated by Django 4.2 on 2023-04-21 10:18

from django.db import migrations, models
import personnelManager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('client_slug', models.SlugField(blank=True, unique=True)),
                ('username', models.CharField(max_length=50, unique=True, validators=[personnelManager.models.validate_letters_and_numbers])),
                ('password', models.CharField(help_text='Enter password for this user.', max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=30, validators=[personnelManager.models.validate_only_letters])),
                ('middle_name', models.CharField(blank=True, max_length=30, validators=[personnelManager.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[personnelManager.models.validate_only_letters])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[personnelManager.models.validate_only_numbers])),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('tax_file_number', models.CharField(blank=True, max_length=9, null=True, validators=[personnelManager.models.validate_only_numbers])),
                ('licence_number', models.CharField(blank=True, max_length=20, null=True, validators=[personnelManager.models.validate_letters_and_numbers])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
