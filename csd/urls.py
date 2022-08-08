from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .api import (AccreditationInfotApiView, CertificateViewSet, ClientViewSet, ContactViewSet,
                  MainInfotApiView, NewsViewSet, ServiceViewSet, OrderApiView)

router = routers.DefaultRouter()
router.register('services', ServiceViewSet, 'Services')
router.register('news', NewsViewSet, 'News')
router.register('accreditation/certificates', CertificateViewSet, 'Certificate')
router.register('clietns', ClientViewSet, 'Clietns')
router.register('main/contacts', ContactViewSet, 'Contacts'),

urlpatterns = router.urls

urlpatterns += [
    path('main/info', MainInfotApiView.as_view()),
    path('accreditation/info', AccreditationInfotApiView.as_view()),
    path('orders/order', OrderApiView.as_view()),
]