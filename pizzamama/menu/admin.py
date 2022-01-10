from django.contrib import admin

from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients','vegeterian','price',)
    search_fields = ['name']

admin.site.register(Pizza,PizzaAdmin)