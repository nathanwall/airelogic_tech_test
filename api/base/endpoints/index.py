""" Index endpoints """
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    """ Index URL """
    return {"title": "airelogic_tech_test"}
