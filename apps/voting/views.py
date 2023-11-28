from django.core.exceptions import ValidationError
from django.db.models import F, Q
from django.shortcuts import render

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Voting, VotingCharacter
from .serializers import VotingSerializer, MakeVotingSerializer, WinnerSerializer
from .serializers import CharacterSerializer
from .services import make_voting
from .models import Character


class CharacterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class VotingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Voting.objects.all().prefetch_related('characters')
    serializer_class = VotingSerializer

    @action(detail=False, methods=['get'])
    def active_votings(self, request):
        """
        Представление для просмотра АКТИВНЫХ голосований
        """
        active_votings = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(active_votings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def inactive_votings(self, request):
        """
        Представление для просмотра НЕАКТИВНЫХ голосований
        """
        inactive_votings = self.get_queryset().filter(is_active=False)
        serializer = self.get_serializer(inactive_votings, many=True)
        return Response(serializer.data)


class WinnerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Представление для отображения победителей голосований"""
    queryset = VotingCharacter.objects.filter(
        Q(num_of_votes=F('voting__early_terminations')) &
        Q(voting__is_active=False)
    )
    serializer_class = WinnerSerializer


class MakeVoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MakeVotingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            make_voting(serializer.validated_data)
        except ValidationError as exception:
            return Response({'message': exception}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Ваш голос учтен'}, status=status.HTTP_201_CREATED)



