"""Example routes. Grouped here so main.py stays small."""

from fastapi import APIRouter

from schemas import Item, Message

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    """Health check - use this to tell if the server is alive."""
    return {"status": "ok"}


@router.get("/hello/{name}")
async def hello(name: str) -> dict[str, str]:
    """Path parameter: GET /hello/Alex  ->  {"message": "Hello, Alex!"}"""
    return {"message": f"Hello, {name}!"}


@router.get("/search")
async def search(q: str, limit: int = 10) -> dict[str, object]:
    """Query parameters: GET /search?q=rice&limit=5"""
    return {"query": q, "limit": limit}


@router.post("/echo", response_model=Message)
async def echo(message: Message) -> Message:
    """Request body: POST /echo  {"text": "hello"}"""
    return message


@router.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item) -> Item:
    """response_model validates and filters what gets sent back."""
    return item
