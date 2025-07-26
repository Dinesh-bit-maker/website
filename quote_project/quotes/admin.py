from django.contrib import admin
from .models import QuoteRequest

# Register your models here.
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_time', 'freight_type', 'distance')
    search_fields = ('name', 'email', 'freight_type')
    list_filter = ('freight_type', 'date_time')
    ordering = ('-date_time',)

