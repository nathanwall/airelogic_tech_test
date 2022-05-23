""" MusicBrainz API models """
from pydantic import BaseModel

# pylint: disable=too-few-public-methods

class Artist(BaseModel):
    """ Artist model from MusicBrainz """
    id: str
    name: str

class GetArtist(BaseModel):
    """ Artist list model from MusicBrainz """
    artists: list[Artist]

class Releases(BaseModel):
    """ Artist release ID model from MusicBrainz """
    id: str

class GetReleases(BaseModel):
    """ Artist releases list model from MusicBrainz """
    releases: list[Releases]

class TrackTitle(BaseModel):
    """ Artist track title model from MusicBrainz """
    title: str

class Tracks(BaseModel):
    """ Artist tracks model from MusicBrainz """
    tracks: list[TrackTitle]

class Media(BaseModel):
    """ Artist media model from MusicBrainz """
    media: list[Tracks]
