from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/",view=views.cadastro, name="cadastro"),
    path("login/",view=views.login, name="login"),
    path("create/",view=views.crud_create, name="create"),
    path("read/",view=views.crud_read, name="read"),
    path("update/",view=views.crud_update, name="update"),
    path("delete/",view=views.crud_delete, name="delete")
]