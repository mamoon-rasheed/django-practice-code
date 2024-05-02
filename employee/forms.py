
from django import forms

from employee.models import Department, Designation, Employee, JobDescription

class DesignationForm(forms.Form):
    title = forms.CharField(max_length=100, label='Title', required=True, help_text='Enter the title of the designation')
    description = forms.CharField(widget=forms.Textarea)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title', 'hire_date', 'salary', 'department', 'designation', 'jobdescription']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'})
        }

        def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['department'].queryset = Department.objects.all()
            self.fields['designation'].queryset = Designation.objects.all()
            self.fields['jobdescription'].queryset = JobDescription.objects.all()