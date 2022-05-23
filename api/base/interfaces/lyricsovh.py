""" lyrics.ovh interface """

import logging
import urllib.parse
from pydantic import ValidationError
import requests
from api.base.models.lyricsovhmodels import Lyrics

# pylint: disable=too-few-public-methods
# pylint: disable=logging-fstring-interpolation

class LyricsOVH():
    """lyrics.ovh API interface """
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {"Accept":"application/json"}

    async def get_lyrics(self, artist: str, track: str) -> str:
        """ Get lyrics for track """
        logging.info(f"Start get_lyrics({artist},{track})")
        artist = urllib.parse.quote(artist)
        track = urllib.parse.quote(track).replace("/", " ")
        qry = f"{self.url}/{artist}/{track}"
        request_result = requests.get(qry, headers=self.headers)
        # Sometimes the API likes to throw a 502 proxy error
        while request_result.status_code == 502:
            # try again
            request_result = requests.get(qry, headers=self.headers)

        try:
            lyrics = Lyrics.parse_obj(request_result.json()).lyrics
        except ValidationError:
            # if we didn't get any lyrics back, set them to blank
            lyrics = ""

        logging.info(f"End get_lyrics({lyrics})")
        return lyrics
