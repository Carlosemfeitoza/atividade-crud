from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quadrinho
from .forms import QuadrinhoForm

class QuadrinhoListView(ListView):
    model = Quadrinho
    template_name = "catalogo/listar.html"
    context_object_name = "quadrinhos"

class QuadrinhoDetailView(DetailView):
    model = Quadrinho
    template_name = "catalogo/detalhe.html"
    context_object_name = "quadrinho"

class QuadrinhoCreateView(CreateView):
    model = Quadrinho
    form_class = QuadrinhoForm
    template_name = "catalogo/form.html"
    success_url = reverse_lazy('quadrinho-lista')

class QuadrinhoUpdateView(UpdateView):
    model = Quadrinho
    form_class = QuadrinhoForm
    template_name = "catalogo/form.html"
    success_url = reverse_lazy('quadrinho-lista')

class QuadrinhoDeleteView(DeleteView):
    model = Quadrinho
    template_name = "catalogo/confirm_delete.html"
    success_url = reverse_lazy('quadrinho-lista')