from rest_framework import serializers
from .models import Voting, Characters, Vote
from apps.characters.serializers import CharacterSerializer


class VotingSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    is_active = serializers.BooleanField(read_only=True)
    winner = CharacterSerializer()

    class Meta:
        model = Voting
        fields = ['id', 'title', 'start_date', 'end_date', 'early_terminations', 'characters', 'is_active', 'winner']


class WinnerSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для отображения победителей
    """
    winner = CharacterSerializer()

    class Meta:
        model = Voting
        fields = ['winner']

