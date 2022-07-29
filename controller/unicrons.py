from fastapi import APIRouter

router = APIRouter(
    prefix="/unicorns",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def get_users():
    return fake_items_db
