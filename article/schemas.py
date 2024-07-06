from ninja import Schema
from pydantic import Field, Required


class ArticleResponseSchema(Schema):
    id: int
    title: str
    content: str


class ArticleCreationSchema(Schema):
    title: str = Field(Required, min_length=1, max_length=255)
    content: str = Field(Required, min_length=1)
