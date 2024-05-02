from django.shortcuts import render

from employee.forms import DesignationForm, EmployeeForm
from employee.models import Department, Designation, Employee, JobDescription

# Create your views here.
def adddepartment(request):
    departmentname_error = ''

    if request.method == 'POST':
        name = request.POST['departmentname']

        if name == "":
            departmentname_error = 'Department name is required'
        else:
            Department.objects.create(name = name)

    context = {
        'departmentname_error': departmentname_error
    }
    return render(request, 'employee/add_department.html', context)

def adddesignation(request):
    designationform = DesignationForm()
    
    if request.method == 'POST':
        designationform = DesignationForm(request.POST)

        if designationform.is_valid():
            title = designationform.cleaned_data['title']
            description = designationform.cleaned_data['description']

            Designation.objects.create(title = title, description = description)

    context = {
        'designationform': designationform
    }

    return render(request, 'employee/add_designation.html', context)

def addemployee(request):
    employeeform = EmployeeForm()

    if request.POST:
        employeeform = EmployeeForm(request.POST)

        if employeeform.is_valid():
            first_name = employeeform.cleaned_data['first_name']
            last_name = employeeform.cleaned_data['last_name']
            job_title = employeeform.cleaned_data['job_title']
            hire_date = employeeform.cleaned_data['hire_date']
            salary = employeeform.cleaned_data['salary']
            department = employeeform.cleaned_data['department']
            designation = employeeform.cleaned_data['designation']
            jobdescription = employeeform.cleaned_data['jobdescription']

            department = Department.objects.get(name = department)
            designation = Designation.objects.get(title = designation)

            employee = Employee.objects.create(first_name = first_name, last_name = last_name, job_title = job_title, hire_date = hire_date, salary = salary, department = department, designation = designation)

            for jd in jobdescription:
                jobdescription = JobDescription.objects.get(description = jd)
                employee.jobdescription.add(jobdescription)
            
    context = {
       'employeeform': employeeform,
    }

    return render(request, 'employee/add_employee.html', context)

