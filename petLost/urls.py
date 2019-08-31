"""petLost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import (
    PetViewSet, BreedViewSet, AnnouncementViewSet, CityViewSet, UserViewSet, BannerViewSet,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="Pet Lost",
      default_version='v1',
      description="Making Pets Happier",
      contact=openapi.Contact(email="guile.hm@hotmail.com"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'pets', PetViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'cities', CityViewSet)
router.register(r'users', UserViewSet)
router.register(r'banners', BannerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls', namespace='web')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
