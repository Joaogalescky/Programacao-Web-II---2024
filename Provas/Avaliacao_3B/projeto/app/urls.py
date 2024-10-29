from django.urls import path
from .views import (
    AutorView, AutorReadUpdateDeleteView, LivroAutorView, LivroAutorReadUpdateDelete
)

urlpatterns = [
    # Endpoints para autor
    path('autores/', AutorView.as_view(), name='autor-list-create'),
    path('autores/<int:pk>/', AutorReadUpdateDeleteView.as_view(), name='autor-read-update-delete'),

    # Endpoints para livro
    path('livros/', LivroAutorView.as_view(), name='livro-list-create'),
    path('livros/<int:pk>/', LivroAutorReadUpdateDelete.as_view(), name='livro-read-update-delete'),
]