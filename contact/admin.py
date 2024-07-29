from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',

# Criando a tabela na admin do django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # o que vamos mostrar no django admin
    list_display = ('first_name', 'last_name', 'phone')
    # método de ordenação
    ordering = ('id',) #('-id') = id descrenscente
    # adcionando um filtro
    #list_filter('created_date',)
    # adcionando um campo de pesquisa
    search_fields = ('id', 'first_name',)
    # quantos registros vão ser mostrados por pagina
    list_per_page = 10
    list_max_show_all = 50
    # informar quais campos podem ser editados
    #list_editable = 'first_name', 'last_name',