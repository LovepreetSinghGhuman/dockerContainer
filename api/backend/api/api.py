from fastapi import APIRouter

from .cat import cat_router
from .joke import joke_router
from .prime import prime_router

api_router = APIRouter(
    prefix="/v1",
)
api_router.include_router(cat_router, prefix="/cats", tags=["cat"])
api_router.include_router(prime_router, prefix="/primes", tags=["primes"])
api_router.include_router(joke_router, prefix="/jokes", tags=["joke"])

