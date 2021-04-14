from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['name']
        email = request.POST['email-address']
        senha = request.POST['password']

        if not nome.strip():
            return redirect('cadastro')

        if not email.strip():
            return redirect('cadastro')

        if senha is None:
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return redirect('login')

    else:
        return render(request, 'login_page/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email-address']
        senha = request.POST['password']

        if email == "" or senha == "":
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = authenticate(request, username=nome, password = senha)

            if user is not None:
                login_auth(request, user)
                return render(request, 'login_page/login_success.html')



    return render(request, 'login_page/login.html')
    print('login falhou')



def login_success(request):
    return render(request, 'login_page/login_success.html')

