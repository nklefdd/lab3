from django.contrib import admin

from .models import Department, FacultyInfo, Program, Teacher

admin.site.site_header = "Адміністрування сайту факультету гуманітарних наук"
admin.site.site_title = "Адмінпанель ФГН"
admin.site.index_title = "Керування сайтом факультету"


@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "description", "contacts"),
                "description": (
                    "На головній сторінці відображається запис з інформацією "
                    "про факультет з найменшим ідентифікатором."
                ),
            },
        ),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "level", "coordinator_name", "department")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")
