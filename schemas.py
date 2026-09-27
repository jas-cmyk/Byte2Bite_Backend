"""Pydantic models used to validate request bodies and document responses."""

from pydantic import BaseModel, Field


class Message(BaseModel):
    """Example request body: POST /echo  {"text": "hello"}"""

    text: str = Field(min_length=1, max_length=500)


class Item(BaseModel):
    """Example response body: what a created item looks like."""

    id: int
    name: str
    price: float
