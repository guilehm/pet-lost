from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('lost/', views.lost_list, name='lost'),
]
