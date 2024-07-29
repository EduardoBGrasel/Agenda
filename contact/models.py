from django.db import models
from django.utils import timezone # para preencher a data de criação
from django.contrib.auth.models import User # importando o user django

#id(primary key)
#First Name (string), Last name (string), phone (string)
#email (email), create date (date), description (text)
#category (foreing key), show (boolean), owner (foreign key)
#picture (image)

class Category(models.Model): # classe category (fk de contact)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):  # ciriação da classe que herda de Modeel
    # define um campo string com tamanho maximo de 50 caracteres
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    # define um campo email 
    email = models.EmailField(max_length=254)
    # define um campo para a data de criação e preenche com um valor imutavel
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) # opção para tornar o campo opcional
    # define se o contato será ou não mostrado
    show = models.BooleanField(default=True)
    # link para uma foto
    image = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # definindo a foreign key para category
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null = True,
                                 blank=True)
    # definindo a foreign key para o owner do contact (user do django)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              null = True,
                              blank=True)

    # o que vai aparecer no django admin
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
