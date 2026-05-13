from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio_home')

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request, user)
            return redirect('portfolio_home')
        else:
            return render(request, 'accounts/login.html', {
                'mensagem': 'Credenciais inválidas. Tente novamente.'
            })

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registo_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio_home')

    form = RegistoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'accounts/registo.html', {'form': form})