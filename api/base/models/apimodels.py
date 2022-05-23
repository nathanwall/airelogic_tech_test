""" airelogic_tech_test API models """
from pydantic import BaseModel

# pylint: disable=too-few-public-methods

class AverageReturnModel(BaseModel):
    """ Return model for /average_lyrics endpoint """
    artist: str
    average: float
