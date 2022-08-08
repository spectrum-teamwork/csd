from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .api import (AccreditationInfotApiView, CertificateViewSet, ClientViewSet, ContactViewSet,
                  MainInfotApiView, NewsViewSet, ServiceViewSet, OrderApiView)

router = routers.DefaultRouter()
router.register('api/v1/services', ServiceViewSet, 'Services')
router.register('api/v1/news', NewsViewSet, 'News')
router.register('api/v1/accreditation/certificates', CertificateViewSet, 'Certificate')
router.register('api/v1/clietns', ClientViewSet, 'Clietns')
router.register('api/v1/main/contacts', ContactViewSet, 'Contacts'),

urlpatterns = router.urls

urlpatterns += [
    path('api/v1/main/info', MainInfotApiView.as_view()),
    path('api/v1/accreditation/info', AccreditationInfotApiView.as_view()),
    path('api/v1/orders/order', OrderApiView.as_view()),
]