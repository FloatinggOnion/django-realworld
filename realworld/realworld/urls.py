from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import UserDetailsView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/users/', include('dj_rest_auth.urls')),
    path('api/users/', include('dj_rest_auth.registration.urls')),
    path('api/user/', UserDetailsView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)