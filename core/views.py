from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Account


def index(request):
    return render(request, 'core/index.html')

def editor_view(request):
    return render(request, 'core/editor.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=password)
            login(request, account)
            messages.success(request, 'Registration Successfull')
            return redirect('editor')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'core/registration.html', context)


'''
registered user can login with his email and password
'''


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('editor')

    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'core/login.html', context)


'''
logged in user can logout
'''


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out', extra_tags='alert')
    return redirect('index')
