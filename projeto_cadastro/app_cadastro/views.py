from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request,'produtos/home.html')

def produtos(request):
   novo_produto = Produto()
   novo_produto.nome = request.POST.get('nome')  #request ele visualiza e ele chama o metodo post no html
   novo_produto.descricao = request.POST.get('descricao')   
   novo_produto.preco = request.POST.get('preco')  
   novo_produto.validade = request.POST.get('validade')

   novo_produto.save()                              #salva no banco de dados

   produtos = dict(
      produtos= Produto.objects.all()    #ele pega todos 
   )

   return render(request,'produtos/produtos.html',produtos)  