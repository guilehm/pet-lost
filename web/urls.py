from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/lost/', views.lost_list, name='pet-lost'),
    path('pets/found/', views.found_list, name='pet-found'),
    path('pets/add/', views.pet_add, name='pet-add'),
    path('pets/owned/', views.pet_list_by_user, name='pet-owned-list'),
    path('pets/<str:slug>/', views.pet_detail, name='pet-detail'),
    path('pets/<str:slug>/change/', views.pet_change, name='pet-change'),
    path('pets/<str:slug>/pictures/upload/', views.pet_pictures_upload, name='pet-pictures-upload'),
    path(
        'pets/<str:slug>/pictures/remove/<int:picture_id>/',
        views.pet_pictures_remove, name='pet-pictures-remove'
    ),
    path(
        'pets/<str:slug>/pictures/profile/change/<int:picture_id>/',
        views.pet_pictures_profile_change, name='pet-pictures-profile-change'
    ),
    path('accounts/profile/', views.profile, name='account-profile'),
    path('accounts/profile/change', views.profile_change, name='account-profile-change'),
    path('accounts/login/', views.login_view, name='account-login'),
    path('accounts/logout/', views.logout_view, name='account-logout'),
    path('accounts/signup/', views.signup_view, name='account-signup'),
    path('accounts/social/login/cancelled/', views.login_view),
    path('announcements/add/', views.announcement_add, name='announcement-add'),
]
