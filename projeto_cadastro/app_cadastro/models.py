from django.db import models

# vai tranformar em create table
# Create your models here.
class Produto (models.Model):
    id_produto = models.AutoField(primary_key=True)         # automatiza o id do cadastro no caso
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco = models.FloatField()
    validade = models.DateField()

