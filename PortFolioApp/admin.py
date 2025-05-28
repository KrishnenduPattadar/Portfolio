from django.contrib import admin

# Register your models here.
from .models import Inquiry
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)
    ordering = ('-id',)

