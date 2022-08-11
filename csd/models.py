from turtle import title
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class ServiceType(models.TextChoices):
    TESTING = 'testing', _('testing')
    CERTIFICATION = 'certification', _('certification')


class InfoType(models.TextChoices):
    MAIN = 'main', _('main')
    ACCREDITATION = 'accreditation', _('accreditation')


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Contact(UUIDMixin):
    region = models.CharField(_('region'), max_length=255)
    city = models.CharField(_('city'), max_length=255)
    address = models.CharField(_('address'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255)
    email = models.EmailField(_('email'), max_length=255)

    place_src = models.CharField(_('place_src'), max_length=255)

    class Meta:
        db_table = "contacts"
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return self.address


class Service(UUIDMixin):
    title = models.CharField(_('title'), max_length=255)
    service_type = models.CharField(_('service_type'), max_length=64, choices=ServiceType.choices, default=ServiceType.TESTING,)
    image = models.ImageField(_('image'), upload_to='images/')
    description = models.TextField(_('description'))
    image_document = models.ImageField(_('image_document'), upload_to='images/')
    requirements = models.TextField(_('requirements'))
    price = models.FloatField(_('price'))

    class Meta:
        db_table = "services"
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.title


class Client(UUIDMixin):  # Клиенты
    title = models.CharField(_('title'), max_length=255)
    image = models.ImageField(_('image'), upload_to='images/')

    class Meta:
        db_table = "clients"
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __str__(self):
        return self.title


class Certificate(UUIDMixin):  # Клиенты
    label = models.CharField(_('label'), max_length=255)
    image = models.ImageField(_('image'), upload_to='images/')

    class Meta:
        db_table = "certificates"
        verbose_name = _('certificate')
        verbose_name_plural = _('certificates')

    def __str__(self):
        return self.label


class News(UUIDMixin):  # Новости
    title = models.CharField(_('title'), max_length=255)
    image = image = models.ImageField(_('image'), upload_to='images/')
    text = models.TextField(_('text'))

    class Meta:
        db_table = "news"
        verbose_name = _('news')
        verbose_name_plural = _('newss')

    def __str__(self):
        return self.title


class Order(UUIDMixin):  # Заявки
    service = models.ForeignKey('Service', on_delete=models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey('Contact', on_delete=models.DO_NOTHING)

    contact_name = models.CharField(_('contact_name'), max_length=255)
    phone = models.CharField(_('contact_name'), max_length=255)
    email = models.CharField(_('contact_name'), max_length=255)
    comment = models.TextField(_('text'))

    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        db_table = "orders"
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return self.contact_name


class Info(UUIDMixin):
    info_type = models.CharField(_('info_type'), max_length=64, choices=InfoType.choices, default=InfoType.MAIN,)
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('text'))

    class Meta:
        db_table = "info"
        verbose_name = _('info')
        verbose_name_plural = _('infos')

        constraints = [
            models.UniqueConstraint(fields=['info_type'], name='info_type_idx')
        ]

    def __str__(self):
        return self.title
