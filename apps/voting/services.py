from dataclasses import dataclass, field
from .models import VotingCharacter


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
    entity = VotingCharacter.objects.filter(character=character, voting=voting).first()
    if entity:
        entity.num_of_votes += 1
        entity.save()
    else:
        VotingCharacter.objects.create(character=character, voting=voting)



    ### DTO НАДО ЗНАТЬ