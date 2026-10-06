from django.shortcuts import get_object_or_404, render

from .models import Department, FacultyInfo, Program


def index(request):
    info = FacultyInfo.objects.order_by("id").first()
    context = {"info": info, "departments": Department.objects.all()}
    return render(request, "faculty/index.html", context)


def program_list(request):
    programs = Program.objects.select_related("department")
    sections = [
        {
            "title": "Перший (бакалаврський) рівень вищої освіти",
            "programs": programs.filter(level="bachelor"),
        },
        {
            "title": "Другий (магістерський) рівень вищої освіти",
            "programs": programs.filter(level="master"),
        },
    ]
    return render(request, "faculty/program_list.html", {"sections": sections})


def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, "faculty/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.all()
    return render(request, "faculty/department_list.html", {"departments": departments})


def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    context = {"department": department}
    return render(request, "faculty/department_detail.html", context)
