from django.db import models
from django.utils import timezone
from personnelManager.models import Employee,Department

# Create your models here.


# class PayrollCategory(models.Model):

#     payroll_cat_slug = models.SlugField(max_length=50, unique=True)
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     dollar_value = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)

# class EmployeeBankaccount(models.Model):
#     bank_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bank_id')
#     bank_name = models.CharField(max_length=50)
#     bsb_number = models.CharField(max_length=50)
#     account_number = models.CharField(max_length=50)
#     account_name = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)


# class PayrollPeriod(models.Model):
#     pass

# class LeaveIntilement(models.Model):
#     leave_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_id')
#     leave_type = models.ForeignKey(PayrollCategory, on_delete=models.CASCADE, related_name='leave_type_id')
#     leave_hrs = models.DecimalField(max_digits=5, decimal_places=2)
#     leave_days = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)


# class Benifits(models.Model):
#     benifits_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='benifits_id')
#     benifits_type = models.ForeignKey(PayrollCategory, on_delete=models.CASCADE, related_name='benifits_type_id')
#     description = models.TextField()
#     dollar_value = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)



# class Deductions(models.Model):
#     deductions_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='deductions_id')
#     deductions_type = models.ForeignKey(PayrollCategory, on_delete=models.CASCADE, related_name='deductions_type_id')
#     description = models.TextField()
#     dollar_value = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)

# class SalaryStructure(models.Model):
#     salary_slug = models.SlugField(max_length=50, unique=True)
#     salary_name = models.CharField(max_length=50)
#     description = models.TextField()
#     gross_per_hour_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     net_per_hour_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)


# class Timesheet(models.Model):
#     timesheet_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='timesheet_id')
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='timesheet_department_id')
#     start_date = models.DateTimeField(default=timezone.now)
#     end_date = models.DateTimeField(default=timezone.now)
#     total_hrs = models.DecimalField(max_digits=5, decimal_places=2)
#     total_days = models.DecimalField(max_digits=5, decimal_places=2)
#     total_weeks = models.DecimalField(max_digits=5, decimal_places=2)
#     total_months = models.DecimalField(max_digits=5, decimal_places=2)
#     total_years = models.DecimalField(max_digits=5, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)


# class Payroll(models.Model):
#     payroll_slug = models.SlugField(max_length=50, unique=True)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_id')
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='payroll_department_id')
#     salary_structure_id = models.ForeignKey(SalaryStructure, on_delete=models.CASCADE, related_name='payroll_salary_structure_id')
#     timesheet_id = models.ForeignKey(Timesheet, on_delete=models.CASCADE, related_name='payroll_timesheet_id')
#     leave_id = models.ForeignKey(LeaveIntilement, on_delete=models.CASCADE, related_name='payroll_leave_id')
#     benifits_id = models.ForeignKey(Benifits, on_delete=models.CASCADE, related_name='payroll_benifits_id')
#     deductions_id = models.ForeignKey(Deductions, on_delete=models.CASCADE, related_name='payroll_deductions_id')
#     gross_pay = models.DecimalField(max_digits=5, decimal_places=2)
#     net_pay = models.DecimalField(max_digits=5, decimal_places=2)
#     total_leave_hrs = models.DecimalField(max_digits=5, decimal_places=2)
#     total_leave_days = models.DecimalField(max_digits=5, decimal_places=2)
#     total_leave_weeks = models.DecimalField(max_digits=5, decimal_places=2)
#     total_leave_months = models.DecimalField(max_digits=5, decimal_places=2)
#     total_leave_years = models.DecimalField(max_digits=5, decimal_places=2)
#     total_benifits = models.DecimalField(max_digits=5, decimal_places=2)
#     total_deductions = models.DecimalField(max_digits=5, decimal_places=2)
#     total_hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
#     total_days_worked = models.DecimalField(max_digits=5, decimal_places=2)
#     total_weeks_worked = models.DecimalField(max_digits=5, decimal_places=2)
#     total_months_worked = models.DecimalField(max_digits=5, decimal_places=2)
#     total_years_worked = models.DecimalField(max_digits=5, decimal_places=2)

#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)

