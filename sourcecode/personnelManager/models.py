from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,User

# Create your models here.
class ClientManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(username, password=password, **extra_fields)

"""
Validator Checks for DataModels

"""
# Validator to check if the fields contains only letters and spaces

def validate_only_letters(value):
    if not all(c.isalpha() or c.isspace() for c in value):
        raise ValidationError(
            _('%(value)s is not a valid name'),
            params={'value': value},
        )
# Validator to check if the username contains only letters and numbers and spaces

def validate_letters_and_numbers(value):
    if not all(c.isalnum() or c.isspace() for c in value):
        raise ValidationError(
            _(f"{value} is not a valid username. The username should contain only letters and numbers."),
            params={'value': value},
        )
        
        
# Validator to check if the fields contains only numbers

def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError(
            _(f"{value} is not a valid input. The field should contain only numbers."),
            params={'value': value},
        )
def validate_unique_licence_number(instance):
    """
    Validates that there is no other non-blank instance of licence_number.
    """
    model = instance.__class__
    existing_licence_numbers = model.objects.exclude(pk=instance.pk).exclude(licence_number='').values_list('licence_number', flat=True)
    if instance.licence_number and instance.licence_number in existing_licence_numbers:
        raise ValidationError('This licence number already exists.')

def validate_unique_tax_file_number(instance):
    """
    Validates that there is no other non-blank instance of tax_file_number.
    """
    model = instance.__class__
    existing_tax_file_numbers = model.objects.exclude(pk=instance.pk).exclude(tax_file_number='').values_list('tax_file_number', flat=True)
    if instance.tax_file_number and instance.tax_file_number in existing_tax_file_numbers:
        raise ValidationError('This tax file number already exists.')
    
"""
DataModels

"""

class Client(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    client_slug = models.SlugField(max_length=50, unique=True, blank=True)
    username = models.CharField(max_length=50, unique=True, validators=[validate_letters_and_numbers])
    password = models.CharField(_('password'), max_length=128, help_text=_('Enter password for this user.'))
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, validators=[validate_only_letters])
    middle_name = models.CharField(max_length=30, blank=True, validators=[validate_only_letters])
    last_name = models.CharField(max_length=30, validators=[validate_only_letters])
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=10, blank=True, validators=[validate_only_numbers])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    tax_file_number = models.CharField(max_length=9, null=True, blank=True, validators=[validate_only_numbers])
    licence_number = models.CharField(max_length=20, null=True, blank=True, validators=[validate_letters_and_numbers])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    objects = ClientManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','password']

    def save(self, *args, **kwargs):
        if self.first_name is not None and self.first_name.strip():
            self.first_name = self.first_name.title()
        if self.middle_name is not None and self.middle_name.strip():
            self.middle_name = self.middle_name.title()
        if self.last_name is not None and self.last_name.strip():
            self.last_name = self.last_name.title()
        super().save(*args, **kwargs)

    def clean(self):
        validate_unique_licence_number(self)
        validate_unique_tax_file_number(self)
    
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Client(), self).save(*args, **kwargs)

    def get_short_name(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    
    # Calculate the age based on the date of birth

        if self.user.date_of_birth:
            today = date.today()
            age = today.year - self.user.date_of_birth.year - ((today.month, today.day) < (self.user.date_of_birth.month, self.user.date_of_birth.day))
            self.age = age
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username

