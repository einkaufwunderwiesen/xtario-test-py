from fastapi import FastAPI
from app.routes import users, posts

app = FastAPI(title="Xtario Test API")

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(posts.router, prefix="/api/posts", tags=["posts"])

@app.get("/health")
async def health():
    return {"status": "ok"}
