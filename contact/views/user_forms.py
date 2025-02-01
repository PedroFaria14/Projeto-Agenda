
from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from contact.forms import RegisterForm, RegisterUpdateForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()
    
    #messages.info(request, 'Texto de informação aqui!')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request ,'Usuario Criado')
            return redirect('contact:login')
    
    return render(request, 'contact/register.html',{
        
        'form': form,
    })

def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com Sucesso!')
            return redirect('contact:index')
        
        # Caso as credenciais sejam inválidas
        messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'contact/login.html', {
        'form': form,
    })
    
    
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
    
@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            auth.login(request, request.user)  # New Login
            messages.success(request, "Atualizado com sucesso.")
            return redirect("contact:user_update")

    return render(
        request,
        "contact/user-update.html",
        {
            "site_title": "Update User - ",
            "form": form,
        },
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')






























