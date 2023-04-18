from django.contrib import admin
from .models import RegistroHistorico, CarrosDentro


class RegistroHistoricoAdmin(admin.ModelAdmin):
    # Define campos a mostrar en la lista de objetos
    list_display = ('car_id','car_placa', 'status', 'ultima_entrada')

    # Define campos a usar en la búsqueda de objetos
    search_fields = ('car_id','car_placa', 'status', 'ultima_entrada')

class CarrosDentroAdmin(admin.ModelAdmin):
    # Define campos a mostrar en la lista de objetos
    list_display = ('id', 'placa', 'ultima_entrada')

    # Define campos a usar en la búsqueda de objetos
    search_fields = ('id', 'placa', 'ultima_entrada')

admin.site.register(RegistroHistorico, RegistroHistoricoAdmin)
admin.site.register(CarrosDentro, CarrosDentroAdmin)
