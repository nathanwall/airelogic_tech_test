""" artist custom libraries """

import logging
from api.base.interfaces.musicbrainz import MusicBrainz
from api.base.interfaces.lyricsovh import LyricsOVH

# pylint: disable=logging-fstring-interpolation

async def get_artist_average(artist: str) -> int:
    """ Get the average number of lyrics for an artist """
    logging.info(f"Start get_artist_average({artist})")

    # Instantiate the Music Brainz interface class
    music_brainz = MusicBrainz("http://musicbrainz.org/ws/2")

    # Get artist ID and 'found' name
    artist_info = await music_brainz.get_artist(artist)
    logging.info(f"Artist name: {artist_info.name}, Artist ID: {artist_info.id}")

    # Get releases of artist
    releases = await music_brainz.get_releases(artist_info.id)
    logging.info(f"Releases: {releases.releases}")

    # Get tracks of releases and a track count
    tracks = await music_brainz.get_songs(releases.releases)
    logging.info(f"Tracks: {tracks}")
    track_count = len(tracks)
    logging.info(f"Track count: {track_count}")

    # Instantiate the lyrics.ovh interface class
    lyricsovh = LyricsOVH("https://api.lyrics.ovh/v1")

    # Get the number of lyrics in all tracks
    total_lyrics_count = 0
    for track in tracks:
        lyrics = await lyricsovh.get_lyrics(artist_info.name, track)
        lyrics_count = len(lyrics.split())
        logging.info(f"Track: {track}, Lyric count: {lyrics_count}")
        total_lyrics_count += lyrics_count

    # Calculate the average
    try:
        average = total_lyrics_count / track_count
    except ZeroDivisionError:
        average = 0

    logging.info(f"End get_artist_average({average})")
    return average
