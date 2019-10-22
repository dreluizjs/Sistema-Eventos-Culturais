from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'usuario'

urlpatterns = [

    path('', views.usuario_list, name='usuario_list'),
    path('cadastrar', views.usuario_create, name='usuario_create'),
    path('<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('<int:pk>/editar/', views.UsuarioUpdate.as_view(), name='usuario_edit'),
    path('<int:pk>/deletar/', views.usuario_delete, name='usuario_delete'),
]
