from django.contrib import admin
from django.urls import path
from convertisseur_app.views import convertir_fichier

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', convertir_fichier, name='convertir'),
]
