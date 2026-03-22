from django.contrib import admin
from .models import Categoria, Produto, Cliente, Morada, Pedido, ItemPedido

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

admin.site.register(Categoria,CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria")
    list_filter = ("categoria",)
    search_fields = ("nome",)

admin.site.register(Produto,ProdutoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data")
    list_filter = ("data",)

admin.site.register(Pedido,PedidoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")

admin.site.register(Cliente,ClienteAdmin)

class MoradaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "rua", "cidade", "codigo_postal")

admin.site.register(Morada)