from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'funcionario'

urlpatterns = [

    path('', views.funcionario_list, name='funcionario_list'),
    #path('cadastro/', views.funcionario_create, name='funcionario_create'),
    path('<int:pk>/', views.funcionario_detail, name='funcionario_detail'),
    path('cadastro/', views.FuncionarioCreate.as_view(), name='funcionario_add'),
    #path('<int:pk>/edit/', views.FuncionarioUpdate.as_view(), name='funcionario_edit'),
]
