from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from django.core.mail import send_mail

from .models import Certificate, Client, Contact, Info, News, Service, InfoType, Order
from .serializers import (CertificateSerializer, ClientSerializer,
                          ContactSerializer, InfoSerializer, NewsSerializer,
                          ServiceSerializer)


class MainInfotApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        todos = Info.objects.filter(info_type=InfoType.MAIN)
        serializer = InfoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccreditationInfotApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request, *args, **kwargs):
        todos = Info.objects.filter(info_type=InfoType.ACCREDITATION)
        serializer = InfoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, format=None):
        d = Order(**request.data)
        d.save()

        send_mail('Новая заявка!', 'NTcn', None, [d.contact.email])

        return Response({'status': 'created'}, status=status.HTTP_201_CREATED)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ServiceSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer


class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CertificateSerializer


class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer
