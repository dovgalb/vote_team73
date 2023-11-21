from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Characters
from .serializers import CharacterSerializer
