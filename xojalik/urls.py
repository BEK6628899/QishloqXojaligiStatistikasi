from django.contrib import admin
from django.urls import path
from Asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('matbuot/', Matbuot.as_view()),
    path('kontakt/', Kontaktlar.as_view()),
    path('yanglik/', Yangliklar.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
