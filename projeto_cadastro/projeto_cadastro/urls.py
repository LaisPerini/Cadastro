from django.urls import path
from app_cadastro import views

urlpatterns = [
    # github.com                 url principal
    #github.com/LaisPerini       rota

    #     rota,view,nome de referencia 
    path('',views.home,name='home'),
    path('produtos/',views.produtos,name='lista_produtos')
]
