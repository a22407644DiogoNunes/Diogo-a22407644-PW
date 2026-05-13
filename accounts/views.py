from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from .forms import RegistoForm
from .models import PerfilUtilizador
import secrets


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

def envia_email(utilizador, email, request):
    token = utilizador.perfilutilizador.token
    link = f"http://{request.get_host()}/accounts/autentica/?token={token}&username={utilizador.username}"
    send_mail(
        subject='Portfolio: Autenticação por Link Mágico',
        message=f'Caro {utilizador.first_name},\n\nClique no link para entrar:\n{link}',
        from_email='email.app@gmail.com',  # substitui pelo teu email
        recipient_list=[email]
    )

def login_magic_link_view(request):
    """Recebe o email e envia o link mágico."""
    mensagem = None

    if request.method == 'POST':
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            perfil, _ = PerfilUtilizador.objects.get_or_create(user=user)
            perfil.token = secrets.token_urlsafe(32)
            perfil.save()

            envia_email(user, email, request)
            mensagem = 'Email enviado! Verifica a tua caixa de correio.'
        else:
            mensagem = 'Não existe nenhum utilizador com esse email.'

    return render(request, 'accounts/login.html', {'mensagem_magic': mensagem})

def autentica_magic_link_view(request):
    """Valida o token e faz login automático."""
    token = request.GET.get('token')
    username = request.GET.get('username')

    try:
        user = User.objects.get(username=username)
        perfil = PerfilUtilizador.objects.get(user=user)

        if perfil.token and perfil.token == token:
            perfil.token = None
            perfil.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('portfolio_home')
        else:
            return render(request, 'accounts/login.html', {
                'mensagem': 'Link inválido ou já utilizado.'
            })
    except (User.DoesNotExist, PerfilUtilizador.DoesNotExist):
        return render(request, 'accounts/login.html', {
            'mensagem': 'Link inválido.'
        })

def registo_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio_home')

    form = RegistoForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        grupo_autores, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo_autores)
        return redirect('login')

    return render(request, 'accounts/registo.html', {'form': form})