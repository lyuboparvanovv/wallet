from fastapi import FastAPI

from api.endpoints import user, card
from db.database import Base, engine


app = FastAPI(
    title="Virtual Wallet API",
    docs_url="/swagger",
)

Base.metadata.create_all(bind=engine)


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(card.router, prefix="/cards", tags=["cards"])





@app.get("/")
async def root():
    return {"message": "Welcome to Virtual Wallet API!"}