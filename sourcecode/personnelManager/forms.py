from django import forms
from django.contrib.auth.models import Group
from .models import Employee

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['name', 'client']

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super(EmployeeForm, self).__init__(*args, **kwargs)
#         if user:
#             employee_group = Group.objects.get(name='employee_group')
#             if employee_group in user.groups.all():
#                 clients = Client.objects.filter(group=employee_group)
#                 self.fields['client'].queryset = clients
#             else:
#                 self.fields['client'].queryset = Client.objects.none()

#     def clean_client(self):
#         client = self.cleaned_data['client']
#         employee_group = Group.objects.get(name='employee_group')
#         if not employee_group.client_set.filter(pk=client.pk).exists():
#             raise forms.ValidationError("The client does not belong to the employee group.")
#         return client
