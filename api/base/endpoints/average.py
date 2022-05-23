""" Average endpoints """
import logging
from fastapi import APIRouter
from api.base.models.apimodels import AverageReturnModel
from api.base.libs.artist import get_artist_average

# pylint: disable=logging-fstring-interpolation

router = APIRouter()

@router.get("/average_lyrics", response_model=AverageReturnModel)
async def average_lyrics(artist: str = "britney spears") -> AverageReturnModel:
    """ Get average of number of lyrics for an artist """
    logging.info(f"Start average_lyrics({artist})")

    avg = await get_artist_average(artist)
    resp = AverageReturnModel(artist=artist, average=avg)

    logging.info(f"End average_lyrics({resp})")
    return resp
