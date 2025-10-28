from django.db import models

class Quadrinho(models.Model):
    EDITORA_CHOICES = [
        ('DC', 'DC Comics'),
        ('MARVEL', 'Marvel Comics'),
        ('OUTRO', 'Outro'),
    ]

    titulo = models.CharField('Título', max_length=200)
    numero = models.PositiveIntegerField('Número', default=1)
    editora = models.CharField('Editora', max_length=10, choices=EDITORA_CHOICES, default='OUTRO')
    autor = models.CharField('Autor / Roteirista', max_length=150)
    data_lancamento = models.DateField('Data de lançamento', null=True, blank=True)
    descricao = models.TextField('Descrição', blank=True)

    def __str__(self):
        return f"{self.titulo} #{self.numero}"
