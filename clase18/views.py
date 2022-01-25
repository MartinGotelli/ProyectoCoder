from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.shortcuts import redirect, render

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'AppCoder/login.html',
                    {'form': form,
                    'error': 'Contraseña o usuario incorrecto'})
        else:
            return render(request, 'AppCoder/login.html',
                    {'form': form,
                    'error': 'Datos incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form': form})