from django.forms import Form, CharField, ImageField, IntegerField, EmailField, Textarea

class CursoForm(Form):
    curso = CharField(widget=Textarea)
    camada = IntegerField(min_value=100)
    
class ProfesorForm(Form):
    # Con las vistas basadas en clases no hace falta!
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)

class AvatarFormulario(Form):
    imagen = ImageField(required=True)
