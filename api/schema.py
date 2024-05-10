import graphene
from django.conf import settings
from api.futhark import Futhark




class Query(graphene.ObjectType):
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    alphabet = graphene.List(graphene.String)
    def resolve_alphabet(self, info, **kwargs):
        futhark = Futhark()
        return futhark.alphabet

    runeplay = graphene.List(
        graphene.String,
        n=graphene.Int(description="Number of runes to play")
    )
    def resolve_runeplay(self, info, **kwargs):
        futhark = Futhark()
        return futhark.rune_play(abs(kwargs.get('n', 0)))

    encrypt = graphene.String(
        text=graphene.String(required=True, description="Text to be encrypted to runes")
    )
    def resolve_encrypt(self, info, **kwargs):
        futhark = Futhark()
        return  futhark.encrypt(kwargs['text'])