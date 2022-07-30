from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=['health'],
    responses={404: {"description": "Not found"}}
)


@router.get("/ping")
async def ping():
    return "ok"


@router.get("/ishealthy")
def is_healthy():
    return "Developer life matter"


@router.get("/dbping")
def db_ping():
    return "db ping"
