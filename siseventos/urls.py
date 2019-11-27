from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    
    path('usuarios/', include('usuario.urls')),  
    path('funcionarios/', include('funcionario.urls')), 
    path('equipamentos/', include('equipamento.urls')), 
    path('eventos/', include('evento.urls')),       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)