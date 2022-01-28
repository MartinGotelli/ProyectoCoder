from django.contrib import admin

from AppCoder.models import Avatar, Corredor, Curso, Hacker, Profesor, Estudiante, Entregable

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Corredor)
admin.site.register(Hacker)
admin.site.register(Avatar)