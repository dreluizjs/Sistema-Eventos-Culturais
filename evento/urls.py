from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'evento'

urlpatterns = [

    path('', views.lista_evento, name='evento_list'),
    path('cadastrar/', views.EventoCreate.as_view(), name='evento_create'),  
    #path('<slug:evento_slug>', views.detalhe_evento, name='evento_detail'),   
    path('<int:pk>/', views.EventoDetail.as_view(), name='evento_detail'),   
    path('<int:pk>/edit/', views.EventoUpdate.as_view(), name='evento_edit'),
    path('<int:pk>/delete/', views.delete_evento, name='evento_delete'),
]
