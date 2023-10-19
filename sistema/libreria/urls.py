from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [path("", views.inicio, name="inicio"),
               path("nosotros", views.nosotros, name="nosotros"),
               path("libros",views.listar, name="listar"),
               path("libros/crear", views.crear, name="crear"),
               path("libros/editar", views.editar, name="editar"),
               path("eliminar/<int:id>", views.eliminar, name="eliminar")
               ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
