from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'funcionario'

urlpatterns = [    
    #Lista todos os funcionários
    #path('', views.funcionario_list, name='funcionario_list'),

    #CRUD
    #path('cadastrar/', views.funcionario_create, name='funcionario_create'),
    #path('<int:pk>/', views.funcionario_detail, name='funcionario_detail'),
    #path('<int:pk>/editar/', views.funcionario_edit, name='funcionario_edit'),
    #path('<int:pk>/deletar/', views.funcionario_delete, name='funcionario_delete'),

    #CRUD VIEW
    path('', views.FuncionarioList.as_view(), name='funcionario_list'),
    path('cadastrar/', views.FuncionarioCreate.as_view(), name='funcionario_create'),
    path('<int:pk>/', views.FuncionarioDetail.as_view(), name='funcionario_detail'),
    path('<int:pk>/editar/', views.FuncionarioUpdate.as_view(), name='funcionario_edit'),
    path('funcionario/<int:pk>/deletar', views.FuncionarioDelete.as_view(), name='funcionario_delete'),    
]
