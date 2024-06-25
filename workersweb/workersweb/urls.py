
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('',include('main.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
