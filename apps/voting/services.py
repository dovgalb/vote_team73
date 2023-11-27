from dataclasses import dataclass, Field, field
from .models import VotingCharacters


@dataclass
class Vote:
    title: str
    members: dict['Character.name', int] = field(default_factory=dict)


@dataclass(frozen=True)
class Character:
    name: str


def make_voting(validated_data):
    """
    Метод вызова бизнес логики
    """
    character = validated_data['character_id']
    voting = validated_data['voting_id']
    character_dto = Character(character.name)
    vote_dto = Vote(voting.title)
    # res = voting(vote_dto, [character_dto])
    entity = VotingCharacters.objects.filter(character=character, voting=voting).first()
    if entity:
        entity.num_of_votes += 1
        entity.save()
    else:
        VotingCharacters.objects.create(character=character, voting=voting)

    ### DTO НАДО ЗНАТЬ