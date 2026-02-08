import sqlite3


from src import entities
from src.config import settings

class LinkRepository:

    def __init__(self):
        self.db_path = settings.sqlite3_db

    def insert(self, data: entities.LinkWithShortenModel):
        """Insert full url and its token."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO short_links (full_url, token) VALUES (?, ?)",
                (str(data.target_link), data.token)
            )
            conn.commit()


    def select_full_url_by_token(self, token: str) -> str | None:
        """Get full url by token."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT full_url
                FROM short_links
                WHERE token = ?
                """,
            (token,))
            result = cursor.fetchone()
        return result


def get_link_repository() -> LinkRepository:
    return LinkRepository()
