from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/lost/', views.lost_list, name='pet-lost'),
    path('pets/found/', views.found_list, name='pet-found'),
    path('pets/<str:slug>/', views.pet_detail, name='pet-detail'),
    path('accounts/login/', views.login_view, name='account-login'),
    path('accounts/logout/', views.logout_view, name='account-logout'),
]
