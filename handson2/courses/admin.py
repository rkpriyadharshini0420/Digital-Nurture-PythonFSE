from django.contrib import admin
from .models import Department, Course, Student, Enrollment

# Registering basic models
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)

# Customizing the Course model in the admin panel
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'credits', 'department']
    search_fields = ['name', 'code']
    list_filter = ['department']