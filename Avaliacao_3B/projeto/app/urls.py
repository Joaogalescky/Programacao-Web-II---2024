from django.urls import path
from .views import (
    AutorView, AutorReadUpdateDeleteView,
    LivroView, LivroCreateWithAutorView, LivroReadUpdateDeleteView,
    TagCreateWithLivroView,
)

urlpatterns = [
    # Endpoints para autor
    path('autores/', AutorView.as_view(), name='autor-list-create'),
    path('autores/<int:id>/', AutorReadUpdateDeleteView.as_view(), name='autor-detail'),

    # Endpoints para livro
    path('livros/', LivroView.as_view(), name='livro-list-create'),
    path('livros/<int:id>/', LivroReadUpdateDeleteView.as_view(), name='livro-detail'),
    path('livros/cadastrar_livros_com_autor/', LivroCreateWithAutorView.as_view(), name='livro-autor-create'),

    # Endpoints para tag
    path('tags/cadastrar_tags_com_livros/', TagCreateWithLivroView.as_view(), name='tag-livro-create'),
]