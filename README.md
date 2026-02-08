# link-compressor

### Required tools

- [uv](https://docs.astral.sh/uv/)
- [sqlite3](https://www.sqlite.org/docs.html)

### Copy local settings

```bash
cp src/.env.local src/.env
```

### Setup

- Dependency installation
```bash
uv sync --all-groups && source .venv/bin/activate
```

- For production env
```bash
uv sync && source .venv/bin/activate
```

### DB init

```bash
inv db.init
```

### Run app

```bash
inv app.run
```

### Run tests

```bash
inv tests.run
```
