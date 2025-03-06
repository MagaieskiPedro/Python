from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_read, name='crud_read'),
    path('novo/',views.crud_create,name='crud_create'),
    path('atualizar/<int:pk>',views.crud_update,name='crud_update'),
    path('deletar/<int:pk>',views.crud_delete,name='crud_delete')
]
