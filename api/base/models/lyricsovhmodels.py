""" request models for lyrics.ovh """
from pydantic import BaseModel

# pylint: disable=too-few-public-methods

class Lyrics(BaseModel):
    """ Lyrics model from lyrics.ovh """
    lyrics: str
