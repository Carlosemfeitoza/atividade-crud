from django.urls import path
from django.contrib import admin
from catalogo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QuadrinhoListView.as_view(), name='quadrinho-lista'),
    path('quadrinho/<int:pk>/', QuadrinhoDetailView.as_view(), name='quadrinho-detalhe'),
    path('quadrinho/adicionar/', QuadrinhoCreateView.as_view(), name='quadrinho-adicionar'),
    path('quadrinho/<int:pk>/editar/', QuadrinhoUpdateView.as_view(), name='quadrinho-editar'),
    path('quadrinho/<int:pk>/excluir/', QuadrinhoDeleteView.as_view(), name='quadrinho-excluir'),
]