from django.shortcuts import render

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Voting
from .serializers import VotingSerializer, WinnerSerializer, MakeVotingSerializer
from .serializers import CharacterSerializer
from .services import make_voting
from .models import Character


class CharacterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class MakeVoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MakeVotingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        make_voting(serializer.validated_data)