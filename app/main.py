from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, transaction
from app.routes import auth, transactions, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracker API",
    description="A Python-based finance tracking system with role-based access",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(analytics.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Finance Tracker API",
        "docs": "Visit /docs to explore the API"
    }