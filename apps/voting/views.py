from django.shortcuts import render

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Voting, Vote
from .serializers import VotingSerializer, WinnerSerializer
from apps.characters.serializers import CharacterSerializer
from ..characters.models import Characters


class VotingViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Voting.objects.all().prefetch_related('characters')
    serializer_class = VotingSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve_winner':
            return WinnerSerializer
        return VotingSerializer

    @action(detail=True, methods=['get'], name='Retrieve Winner')
    def retrieve_winner(self, request, pk=None):
        voting = self.get_object()
        serializer = self.get_serializer(voting)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], name='Vote')
    def vote(self, request, pk=None):
        voting = self.get_object()
        character_id = request.data.get('character_id')
        try:
            character = Characters.objects.get(pk=character_id)
            Vote.objects.create(voting=voting, character=character)
            return Response({'status': 'vote counted'})
        except Characters.DoesNotExist:
            return Response({'status': 'not a valid character for this voting'}, status=400)
        except ValueError as e:
            return Response({'status': str(e)}, status=400)


class CharacterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer

