from dataclasses import dataclass, Field, field


@dataclass
class Vote:
    title: str
    members: dict['Character.name', int] = field(default_factory=dict)


@dataclass(frozen=True)
class Character:
    name: str


def voting(vote: Vote, members_list: list[Character]):
    """
    Создает голосование
    """
    for member in members_list:
        if member.name not in vote.members:
            vote.members[member.name] = 0
        vote.members[member.name] += 1
    return vote


def make_voting(validated_data):
    """
    Метод вызова бизнеслогики
    """
    member = validated_data['member_id']
    vote = validated_data['vote_id']
    character_dto = Character(member.name)
    vote_dto = Vote(vote.title)
    res = voting(vote_dto, [character_dto])
    entity = throw_table_vaoting_characters.objects.filter(member=member, vote=vote).first()
    if entity:
        entity.amount = res.members[member.name]
        entity.save()
    else:
        throw_table_vaoting_characters.objects.create(member=member, vote=vote, amount=res.members[member.name])

    ### DTO НАДО ЗНАТЬ