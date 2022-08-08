from django.contrib import admin

from .models import Certificate, Client, Contact, Info, News, Order, Service


@admin.register(Info)
class InfoeAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)


@admin.register(Client)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)


@admin.register(News)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('id', 'address',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    search_fields = ('id', 'label',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('id', 'contact_name',)
