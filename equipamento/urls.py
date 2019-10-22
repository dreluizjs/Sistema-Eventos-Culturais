from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'equipamento'

urlpatterns = [
 #CRUD VIEW
    path('', views.EquipamentoList.as_view(), name='equipamento_list'),
    path('cadastrar/', views.EquipamentoCreate.as_view(), name='equipamento_create'),
    path('<int:pk>/', views.EquipamentoDetail.as_view(), name='equipamento_detail'),
    path('<int:pk>/editar/', views.EquipamentoUpdate.as_view(), name='equipamento_edit'),
    path('equipamento/<int:pk>/deletar', views.EquipamentoDelete.as_view(), name='equipamento_delete'),    
]
