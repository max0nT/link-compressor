import typing
import fastapi

from src import entities, repo

from src.short_url import generate_short_link, get_url_by_link

router = fastapi.APIRouter(prefix="", tags=["Link"])


@router.post(
    path="/shorten/",
    response_model=entities.LinkWithShortenModel,
    status_code=fastapi.status.HTTP_201_CREATED
)
async def shorten(
    link_repo: typing.Annotated[
        repo.LinkRepository,
        fastapi.Depends(repo.get_link_repository),
    ],
    data: entities.LinkModel,
) -> entities.LinkWithShortenModel:
    """Generate shorten link."""
    return generate_short_link(url=data.target_url, link_repo=link_repo)


@router.get(
    path="/link/{token}/",
    status_code=fastapi.status.HTTP_308_PERMANENT_REDIRECT,
)
async def redirect_by_token(
    link_repo: typing.Annotated[
        repo.LinkRepository,
        fastapi.Depends(repo.get_link_repository),
    ],
    token: str,
) -> fastapi.responses.RedirectResponse:
    """Redirect to full url by token,"""
    full_url = get_url_by_link(token=token, link_repo=link_repo)
    if not full_url:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=entities.ErrorModel(
                code="not_found",
                detail=f"Cannot find full url with token {token}"
            ).model_dump(),
        )
    return fastapi.responses.RedirectResponse(
        full_url[0],
        status_code=fastapi.status.HTTP_308_PERMANENT_REDIRECT,
    )
