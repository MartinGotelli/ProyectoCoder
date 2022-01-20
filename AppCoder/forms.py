from django.forms import Form, CharField, IntegerField, EmailField

class CursoForm(Form):
    curso = CharField()
    camada = IntegerField()

class ProfesorForm(Form):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)