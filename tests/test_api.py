""" pytest test for API """

from fastapi.testclient import TestClient
from api import app

client  = TestClient(app)

def test_root():
    """ / GET """
    response = client.get("/")
    assert response.status_code == 200

def test_average_lyrics():
    """ /average_lyrics GET"""
    param = "artist=britney spears"
    response = client.get("/average_lyrics", params=param)
    assert response.status_code == 200
    assert "artist" in response.json()
    assert "average" in response.json()

def test_artist_not_found():
    """ /average_lyrics GET test unknown artist """
    param = "artist=pqowiepoqwiewee"
    response = client.get("/average_lyrics", params=param)
    assert response.status_code == 404
    assert response.json()["detail"] == "Artist not found"
