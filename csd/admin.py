from django.contrib import admin

from .models import Certificate, Client, Contact, Info, News, Order, Service


@admin.register(Info)
class InfoeAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(Client)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(News)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    search_fields = ('id', 'label',)
    change_list_template = "admin/model_change_list.htm"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('id', 'contact_name',)
    change_list_template = "admin/model_change_list.htm"
