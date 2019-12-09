from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'evento'

urlpatterns = [

    path('', views.evento_list, name='evento_list'),
    path('cadastrar/', views.evento_create, name='evento_create'),
    #path('cadastrar/', views.EventoCreate.as_view(), name='evento_create'),  
    #path('<slug:evento_slug>', views.evento_detail, name='evento_detail'),   
    path('<int:pk>/', views.EventoDetail.as_view(), name='evento_detail'),   
    path('<int:pk>/editar/', views.EventoUpdate.as_view(), name='evento_edit'),
    path('<int:pk>/deletar/', views.evento_delete, name='evento_delete'),

    ##### DESPESAS DOS EVENTOS #####
    #path('<slug:evento_slug>/despesas/', views.despesa_evento, name='evento_despesa'),
    path('<int:pk>/despesas/', views.despesa_evento2, name='evento_despesa'),
    path('despesa/', views.DespesaList.as_view(), name='despesa_list'),
    path('cadastrar/despesa', views.despesa_create, name='despesa_create'), 
]
