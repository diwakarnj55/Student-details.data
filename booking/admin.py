from django.contrib import admin
from . models import Course, Student, Report, Fees, Exam

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Report)
admin.site.register(Fees)
admin.site.register(Exam)

