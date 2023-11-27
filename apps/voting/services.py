from dataclasses import dataclass, field

from django.core.exceptions import ValidationError

from .models import VotingCharacter
import datetime
import pytz

utc=pytz.UTC


@dataclass
class Vote:
    title: str
    members: dict['Character.name', int] = field(default_factory=dict)


@dataclass(frozen=True)
class Character:
    name: str


def _check_required_amount(voting_character, voting):
    """
    Служебный метод проверки кол-ва голосов
    """
    if voting.early_terminations <= voting_character.num_of_votes:
        voting.is_active = False
        voting.end_date = datetime.datetime.now()
        voting.save()
        raise ValidationError('Превышено максимальное количество голосов')


def _check_expire_date(voting):
    """
    Служебный метод проверки актуальности даты
    """
    current_date = datetime.datetime.now().replace(tzinfo=utc)
    start_date = voting.start_date.replace(tzinfo=utc)
    end_date = voting.end_date.replace(tzinfo=utc)
    if not start_date < current_date <= end_date:
        voting.is_active = False
        voting.save()
        raise ValidationError('Истекла дата голосования')


def make_voting(validated_data):
    """
    Метод вызова бизнес логики
    """
    character = validated_data['character_id']
    voting = validated_data['voting_id']
    voting_character = VotingCharacter.objects.filter(character=character, voting=voting).first()
    if voting_character:
        _check_expire_date(voting)
        _check_required_amount(voting_character, voting)
        voting_character.num_of_votes += 1
        voting_character.save()
        voting.save()
    else:
        VotingCharacter.objects.create(character=character, voting=voting)
