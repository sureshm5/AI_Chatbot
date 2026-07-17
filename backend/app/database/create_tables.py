from app.database.database import engine
import app.models
from app.models.base import Base

Base.metadata.create_all(bind=engine)

print("✅ Tables Created")