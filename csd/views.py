from django.http import FileResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view

def images(request, image_name):
    return FileResponse(open(f'images/{image_name}', 'rb'))
