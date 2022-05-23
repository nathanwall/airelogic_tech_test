""" MusicBrainz interfaces """

import logging
import urllib.parse
from time import sleep
import requests
from fastapi import HTTPException
from api.base.models.musicbrainzmodels import GetArtist, Artist, GetReleases, Media

# pylint: disable=logging-fstring-interpolation

class MusicBrainz():
    """ MusicBrainz API interface """
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {"Accept":"application/json"}

    async def get_artist(self, artist: str) -> Artist:
        """ Get the artist info """
        logging.info(f"Start get_artist({artist})")
        artist = urllib.parse.quote(artist)

        # Make the request
        qry = f"{self.url}/artist/?query=artist:{artist}&limit=1"
        request_result = requests.get(qry, headers=self.headers)

        # Parse the results
        try:
            results = GetArtist.parse_obj(request_result.json()).artists[0]
        except IndexError as exception:
            raise HTTPException(status_code=404, detail="Artist not found") from exception

        artist = Artist.parse_obj(results)

        logging.info(f"End get_artist({artist})")
        return artist

    async def get_releases(self, artist_id: str) -> GetReleases:
        """ Get the releases info for the artist """
        logging.info(f"Start get_releases({artist_id})")

        # Only looking for official albums and EPs
        qry = f"{self.url}/release/?artist={artist_id}&type=album|ep&status=official"
        request_result = requests.get(qry, headers=self.headers)

        # Parse the results
        releases = GetReleases.parse_obj(request_result.json())

        logging.info(f"End get_releases({releases})")
        return releases

    async def get_songs(self, releases: GetReleases) -> list:
        """ Get the song names from the artists releases """
        logging.info(f"Start get_songs({releases})")

        all_tracks = []
        for release in releases:
            # Sleep to avoid rate limiting
            sleep(1)
            qry = f"{self.url}/release/{release.id}?inc=recordings"
            request_result = requests.get(qry, headers=self.headers)

            # Parse the results
            result = Media.parse_obj(request_result.json())
            tracks = result.media[0].tracks
            # Build up a list of individual tracks and filter out duplicates
            for track in tracks:
                if track.title not in all_tracks:
                    all_tracks.append(track.title)

        logging.info(f"End get_songs({all_tracks})")
        return all_tracks
