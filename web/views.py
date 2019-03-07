from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from pet.models import Pet
from petLost.settings import GOOGLE_RECAPTCHA_SITE_KEY
from users.models import User
from web.forms import (
    AddressDataForm, AnnouncementForm, AuthenticationForm, ContactDataForm, PersonalDataForm, PetAddForm,
    SocialDataForm, UserCreationForm,
)
from web.utils import check_recaptcha


def index(request):
    lost = set(Pet.objects.lost().order_by('?').select_related('picture')[:4])
    found = set(Pet.objects.found().order_by('?').select_related('picture')[:4])
    return render(request, 'web/index.html', {
        'pets_lost': lost,
        'pets_found': found,
    })


def lost_list(request):
    lost_qs = Pet.objects.lost().select_related('picture')

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
    found_qs = Pet.objects.found().select_related('picture')

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
    owner = False
    if pet in Pet.objects.filter(user=request.user):
        owner = True
    return render(request, 'web/pet_detail.html', {
        'pet': pet,
        'owner': owner,
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


@check_recaptcha
def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
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
        'form': form,
        'site_key': GOOGLE_RECAPTCHA_SITE_KEY,
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


@login_required
def profile_change(request):
    user = request.user
    try:
        social_account = SocialAccount.objects.get(user=user)
    except SocialAccount.DoesNotExist:
        social_account = None

    personal_data_form = request.GET.get('personal_data')
    address_data_form = request.GET.get('address_data')
    contact_data_form = request.GET.get('contact_data')
    social_media_data_form = request.GET.get('social_media_data')

    if personal_data_form:
        personal_data_form = PersonalDataForm()
        if request.method == 'POST':
            personal_data_form = PersonalDataForm(data=request.POST, instance=user)
            if not personal_data_form.is_valid():
                messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro! Por favor revise todos os dados.')
            else:
                personal_data_form.save()
                messages.add_message(request, messages.SUCCESS, 'Dados pessoais alterados com sucesso.')
                return redirect('web:account-profile')

    if address_data_form:
        address_data_form = AddressDataForm()
        if request.method == 'POST':
            address_data_form = AddressDataForm(data=request.POST, instance=user)

            if not address_data_form.is_valid():
                messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro!')
            else:
                address_data_form.save()
                messages.add_message(request, messages.SUCCESS, 'Dados de endereço alterados com sucesso.')
                return redirect('web:account-profile')

    if contact_data_form:
        contact_data_form = ContactDataForm()
        if request.method == 'POST':
            contact_data_form = ContactDataForm(data=request.POST, instance=user)

            if not contact_data_form.is_valid():
                messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro!')
            else:
                contact_data_form.save()
                messages.add_message(request, messages.SUCCESS, 'Dados de contato alterados com sucesso.')
                return redirect('web:account-profile')

    if social_media_data_form:
        social_media_data_form = SocialDataForm()
        if request.method == 'POST':
            social_media_data_form = SocialDataForm(data=request.POST, instance=user)

            if not social_media_data_form.is_valid():
                messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro!')
            else:
                social_media_data_form.save()
                messages.add_message(request, messages.SUCCESS, 'Dados de redes sociais alterados com sucesso.')
                return redirect('web:account-profile')

    change_form = any([
        personal_data_form, address_data_form, contact_data_form, social_media_data_form
    ])

    return render(request, 'accounts/profile.html', {
        'user': user,
        'social_account': social_account,
        'personal_data_form': personal_data_form,
        'address_data_form': address_data_form,
        'contact_data_form': contact_data_form,
        'social_media_data_form': social_media_data_form,
        'change_form': change_form,
    })


def announcement_add(request):
    pets = Pet.objects.filter(user=request.user)
    if not pets:
        return redirect('web:pet-add')
    announcement_form = AnnouncementForm()
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST)
        if not announcement_form.is_valid():
            messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro!')
        else:
            announcement_form.save()
            messages.add_message(request, messages.SUCCESS, 'Anúncio criado com sucesso.')
    return render(request, 'web/announcement_add.html', {
        'announcement_form': announcement_form,
        'pets': pets,
    })


def pet_add(request):
    pet_form = PetAddForm()
    if request.method == 'POST':
        pet_form = PetAddForm(request.POST)
        if not pet_form.is_valid():
            messages.add_message(request, messages.ERROR, 'Ops, ocorreu um erro!')
        else:
            pet = pet_form.save(commit=False)
            pet.user = request.user
            pet.save()
            messages.add_message(request, messages.SUCCESS, 'Pet cadastrado com sucesso.')
            return redirect('web:pet-detail', pet.slug)

    return render(request, 'web/pet_add.html', {
        'pet_form': pet_form,
    })
