import shortuuid

from src.config import settings
from src.entities import LinkWithShortenModel
from src.repo import LinkRepository

def generate_short_link(url: str, link_repo: LinkRepository) -> LinkWithShortenModel:
    """Generate and save in db token for url"""
    url_token = shortuuid.ShortUUID().random(length=settings.token_url_length)
    url_data = LinkWithShortenModel(target_link=url, token=url_token)
    link_repo.insert(url_data)
    return url_data

def get_url_by_link(token: str, link_repo: LinkRepository) -> str | None:
    return link_repo.select_full_url_by_token(token)

