from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.analytics import get_stats

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/")

def analytics(
    db: Session = Depends(get_db)
):

    return get_stats(db)