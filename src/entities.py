import pydantic
import pydantic.networks

class LinkModel(pydantic.BaseModel):
    """Pydantic class to describe url data for shorting."""

    target_url: pydantic.networks.HttpUrl


class LinkWithShortenModel(LinkModel):
    """Pydantic model to describe url with its shorten version."""

    token: str


class ErrorModel(pydantic.BaseModel):
    """Pydantic Model to describe client errors."""

    code: str
    detail: str
