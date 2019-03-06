from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from pet.models import Pet
from users.models import User
from web.forms import AuthenticationForm, UserCreationForm


def index(request):
    lost = Pet.objects.filter(
        situation=Pet.SITUATION_LOST,
        rescued=False,
    ).order_by('?').select_related('picture')[:4]
    found = Pet.objects.filter(
        situation=Pet.SITUATION_FOUND,
        rescued=False,
    ).order_by('?').select_related('picture')[:4]
    return render(request, 'web/index.html', {
        'pets_lost': lost,
        'pets_found': found,
    })


def lost_list(request):
    lost_qs = Pet.objects.filter(
        situation=Pet.SITUATION_LOST,
        rescued=False,
    ).select_related('picture')

    page = request.GET.get('page')
    paginator = Paginator(lost_qs, 8)
    try:
        lost = paginator.page(page)
    except PageNotAnInteger:
        lost = paginator.page(1)
    except EmptyPage:
        lost = paginator.page(paginator.num_pages)

    return render(request, 'web/pet_list.html', {
        'pets': lost,
        'lost': True,
    })


def found_list(request):
    found_qs = Pet.objects.filter(
        situation=Pet.SITUATION_FOUND,
        rescued=False,
    ).select_related('picture')

    page = request.GET.get('page')
    paginator = Paginator(found_qs, 8)
    try:
        found = paginator.page(page)
    except PageNotAnInteger:
        found = paginator.page(1)
    except EmptyPage:
        found = paginator.page(paginator.num_pages)

    return render(request, 'web/pet_list.html', {
        'pets': found,
        'found': True,
    })


def pet_detail(request, slug):
    pet = get_object_or_404(
        Pet.objects.prefetch_related('pictures'),
        slug=slug,
    )
    return render(request, 'web/pet_detail.html', {
        'pet': pet,
    })


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                email=request.POST['email'],
                password=request.POST['password'],
            )
            if not authenticated_user:
                try:
                    User.objects.get(email=request.POST['email'])
                except User.DoesNotExist:
                    form.add_error('email', 'Nenhum usuário cadastrado com este email')
                else:
                    form.add_error(None, 'Usuário ou senha inválidos')
            else:
                login(
                    request,
                    authenticated_user,
                    backend='django.contrib.auth.backends.ModelBackend',
                )
                return redirect('web:account-login')
    return render(request, 'accounts/login.html', {
        'login_form': form,
    })


def logout_view(request):
    logout(request)
    return redirect('web:index')


def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.save()
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend',
            )
    return render(request, 'accounts/signup.html', {
        'form': form
    })


@login_required
def profile(request):
    user = request.user
    try:
        social_account = SocialAccount.objects.get(user=user)
    except SocialAccount.DoesNotExist:
        social_account = None
    return render(request, 'accounts/profile.html', {
        'user': user,
        'social_account': social_account,
    })
