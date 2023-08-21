from django.urls import path
from . import views

urlpatterns = [
    path('categoria_list/', views.categoria_list,name='categoria_list'),
    
    # URLs para Categoria de Computador
    
    path('categoria_computador/', views.categoria_computador_list, name='categoria_computador_list'),
    path('categoria_computador/create/', views.categoria_computador_create, name='categoria_computador_create'),
    path('categoria_computador/update/<int:pk>/', views.categoria_computador_update, name='categoria_computador_update'),

    # URLs para Localização
    path('localizacao/', views.localizacao_list, name='localizacao_list'),
    path('localizacao/create/', views.localizacao_create, name='localizacao_create'),
    path('localizacao/update/<int:pk>/', views.localizacao_update, name='localizacao_update'),

    # URLs para Computador
    path('computador/create/', views.computador_create, name='computador_create'),
    # URLs para Fila
    path('fila/create/', views.fila_create, name='fila_create'),
]
