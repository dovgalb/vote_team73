from rest_framework import serializers
from .models import Voting, Characters, Vote
from apps.characters.serializers import CharacterSerializer
from django.shortcuts import get_object_or_404

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


#  модернизированные
class MakeVotingSerializer(serializers.Serializer):
    vote_id = serializers.IntegerField()
    member_id = serializers.IntegerField()

    def validate_vote_id(self, vote_id):
        return get_object_or_404(Voting, id=vote_id)

    def validate_member_id(self, member_id):
        return get_object_or_404(Characters, id=member_id)
