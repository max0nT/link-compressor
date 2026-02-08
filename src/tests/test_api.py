import fastapi
import httpx

from src.entities import LinkModel, LinkWithShortenModel
from src import repo

async def test_generate_token(
    test_url: str,
    api_client: httpx.AsyncClient,
    link_repo: repo.LinkRepository,
) -> None:
    """Test generate short token for url works."""
    # TODO get rid off token create duplicate
    data = LinkModel(target_url=test_url).model_dump()
    data["target_url"] = str(data["target_url"])
    response = await api_client.post(
        "/shorten/",
        json=data,
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED
    response = LinkWithShortenModel.model_validate_json(response.content)

    # Check token in saved in db
    raw_url_data = link_repo.select_full_url_by_token(response.token)
    assert raw_url_data
    assert raw_url_data[0] == str(response.target_url)


async def test_redirect(
    test_url: str,
    api_client: httpx.AsyncClient,
) -> None:
    """Test to check redirect via token works correctly."""
    data = LinkModel(target_url=test_url).model_dump()
    data["target_url"] = str(data["target_url"])
    response = await api_client.post(
        "/shorten/",
        json=data,
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED
    response = LinkWithShortenModel.model_validate_json(response.content)

    redirect_response = await api_client.get(
        f"/link/{response.token}/",
    )
    assert (
        redirect_response.status_code
        == fastapi.status.HTTP_308_PERMANENT_REDIRECT
    )
    assert redirect_response.headers["location"] == test_url
