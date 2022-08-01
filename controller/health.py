from fastapi import APIRouter, status

router = APIRouter(
    prefix="/health",
    tags=['health'],
    responses={404: {"description": "Not found"}}
)


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return "ok"


@router.get("/ishealthy", status_code=status.HTTP_200_OK)
def is_healthy():
    return "Developer life matter"


@router.get("/dbping", status_code=status.HTTP_200_OK)
def db_ping():
    return "db ping"
