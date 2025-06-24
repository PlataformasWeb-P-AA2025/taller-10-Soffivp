from django.contrib import admin


from ordenamiento.models import *

# Register your models here.
class ParroquiaAdmin(admin.ModelAdmin):

    list_display = ('nombre','ubicacion')
    search_fields = ('nombre','ubicacion')


class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre','numero_viviendas')
    search_fields = ('nombre','numero_viviendas')



admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
