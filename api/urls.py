from    django.urls import path
from . import views

urlpatterns = [
 
    path('livros/', views.getLivros),
    path('livros/<int:pk>/', views.livroById),
    
]


