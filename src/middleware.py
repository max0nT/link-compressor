import logging
from fastapi import Request
import fastapi

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def track_link_creation(request: Request, call_next):
    """Log short link create"""

    response = await call_next(request)

    if (
        request.method == "POST"
        and "/shorten/" in str(request.url)
        and response.status_code == fastapi.status.HTTP_201_CREATED
    ):
        logger.debug(
            f"Link creation request | "
            f"Path: {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Client: {request.client.host if request.client else 'unknown'}"
        )
    return response
