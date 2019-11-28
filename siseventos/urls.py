from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    
    #### Urls dos aplicativos do Sistema ####
    path('usuarios/', include('usuario.urls')),  
    path('funcionarios/', include('funcionario.urls')), 
    path('equipamentos/', include('equipamento.urls')), 
    path('eventos/', include('evento.urls')),       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)