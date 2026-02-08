from src.repo import get_link_repository

repo = get_link_repository()

print(repo.select_full_url_by_token("U5h3tGzP")[0])
