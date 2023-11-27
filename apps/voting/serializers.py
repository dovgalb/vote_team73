from rest_framework import serializers
from .models import Voting, Character
from django.shortcuts import get_object_or_404


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'age']


class VotingSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Voting
        fields = ['id', 'title', 'start_date', 'end_date', 'early_terminations', 'characters', 'is_active']



#  модернизированные
class MakeVotingSerializer(serializers.Serializer):
    voting_id = serializers.IntegerField()
    character_id = serializers.IntegerField()

    def validate_voting_id(self, voting_id):
        return get_object_or_404(Voting, id=voting_id)

    def validate_character_id(self, character_id):
        return get_object_or_404(Character, id=character_id)
