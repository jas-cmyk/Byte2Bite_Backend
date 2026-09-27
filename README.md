# Byte2Bite Backend

A minimal FastAPI starter, kept small on purpose so it's easy to read.

## Run it

```bash
.venv\Scripts\python main.py
```

Then open http://localhost:8000/docs for the interactive Swagger UI.

## Files

| File             | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `main.py`        | Creates the app, adds CORS, includes routers, starts server |
| `config.py`      | Settings read from `.env`                            |
| `schemas.py`     | Pydantic models for request/response bodies          |
| `routers/home.py`| The example endpoints                                |

## Try the endpoints

```bash
curl http://localhost:8000/health
curl http://localhost:8000/hello/Alex
curl "http://localhost:8000/search?q=rice&limit=5"
curl -X POST http://localhost:8000/echo -H "Content-Type: application/json" -d '{"text":"hello"}'
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"id":1,"name":"Rice","price":4.5}'
```

## The four things worth learning

1. **Path parameters** — `@router.get("/hello/{name}")` with `name: str`
2. **Query parameters** — `search(q: str, limit: int = 10)`
3. **Request bodies** — a Pydantic model as the function argument (`Message`)
4. **Response models** — `response_model=Item` filters the output

`schemas.py` uses `Field(min_length=1)`. Send `{"text": ""}` to `/echo` and you get a
`422` with a description of exactly what was wrong — validation is free with Pydantic.

## Next steps, when you're ready

- Add a router file per feature: `routers/items.py`, `routers/users.py`
- Add a database: `sqlalchemy[asyncio]` + `aiosqlite`, with a `get_db` dependency
- Add auth: `OAuth2PasswordBearer` and a login route

Note: the original `index.py` is still in the folder but is unused — `main.py` replaces it.
