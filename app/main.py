from fastapi import FastAPI
from app.database import engine, Base

# This will import models so SQLAlchemy knows about them
from app.models import user, transaction

# Create all tables in the database automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracker API",
    description="A Python-based finance tracking system with role-based access",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Finance Tracker API",
        "docs": "Visit /docs to explore the API"
    }