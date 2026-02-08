import uuid

import pytest
import httpx

import pytest_mock


from src import repo
from src.main import app


@pytest.fixture(autouse=True)
def mock_db_path(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "src.config.settings.sqlite3_db",
        "test.db"
    )


@pytest.fixture
def api_client() -> httpx.AsyncClient:
    """Return api for testing"""
    return httpx.AsyncClient(
        transport=httpx.ASGITransport(
            app=app,
        ),
        base_url="http://api.com"
    )

@pytest.fixture
def link_repo() -> repo.LinkRepository:
    """Get link repository."""
    return repo.get_link_repository()

@pytest.fixture
def test_url() -> str:
    """Return test url"""
    return f"https://{uuid.uuid4()}.com/"
