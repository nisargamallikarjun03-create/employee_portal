from django.shortcuts import render

employees = [
    {
        'id': 101,
        'name': 'Rahul',
        'department': 'IT',
        'designation': 'Python Developer'
    },
    {
        'id': 102,
        'name': 'Priya',
        'department': 'HR',
        'designation': 'HR Executive'
    },
    {
        'id': 103,
        'name': 'Amit',
        'department': 'Finance',
        'designation': 'Accountant'
    },
    {
        'id': 104,
        'name': 'Sneha',
        'department': 'Marketing',
        'designation': 'Marketing Executive'
    },
    {
        'id': 105,
        'name': 'Kiran',
        'department': 'IT',
        'designation': 'Django Developer'
    }
]


def home(request):
    return render(request, 'home.html')


def employee_list(request):
    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })


def employee_detail(request, id):
    for employee in employees:
        if employee['id'] == id:
            return render(request, 'employees/employee_detail.html', {
                'employee': employee
            })

    return render(request, 'employees/employee_detail.html', {
        'employee': None
    })


def about(request):
    return render(request, 'about.html')