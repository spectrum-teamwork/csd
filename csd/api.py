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
    authentication_classes = []

    def post(self, request: Request, format=None):
        rdat = request.data
        if rdat.get('agree') is not None:
            del rdat['agree']
        d = Order(**rdat)
        d.save()
        text = f'''
        Услуга: {d.service.title if d.service_id is not None else 'Не указана'}
        Имя: {d.contact_name if d.contact_name is not None else 'Не указано'}
        E-mail: {d.email if d.email is not None else 'Не указана'} 
        Телефон: {d.phone if d.phone is not None else 'Не указан'}  
        Комментарий: {d.comment if d.comment is not None else 'Не указан'}'''

        send_mail('Новая заявка!', text, None, [d.contact.email])

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
    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        for d in serializer.data:
            d['text'] = d['text'][:100] + '...'
        return Response(serializer.data)


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
