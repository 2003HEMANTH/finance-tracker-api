from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.models.transaction import TransactionType
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse
)
from app.services.transaction_service import (
    create_transaction,
    get_all_transactions,
    get_transaction_by_id,
    update_transaction,
    delete_transaction
)
from app.services.auth_service import get_current_user, require_role
from datetime import date
from typing import Optional, List

router = APIRouter(prefix="/transactions", tags=["Transactions"])


# ─── Create Transaction (Admin only) ─────────────────────────────

@router.post("/", response_model=TransactionResponse, status_code=201)
def create(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.admin))
):
    """Create a new transaction — Admin only"""
    return create_transaction(db, data, current_user)


# ─── Get All Transactions (All roles) ────────────────────────────

@router.get("/", response_model=List[TransactionResponse])
def get_all(
    transaction_type: Optional[TransactionType] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all transactions with optional filters — All roles"""
    return get_all_transactions(
        db, current_user, transaction_type, category, start_date, end_date
    )


# ─── Get Single Transaction (All roles) ──────────────────────────

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_one(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a single transaction by ID — All roles"""
    return get_transaction_by_id(db, transaction_id)


# ─── Update Transaction (Admin only) ─────────────────────────────

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update(
    transaction_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.admin))
):
    """Update a transaction — Admin only"""
    return update_transaction(db, transaction_id, data, current_user)


# ─── Delete Transaction (Admin only) ─────────────────────────────

@router.delete("/{transaction_id}")
def delete(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.admin))
):
    """Delete a transaction — Admin only"""
    return delete_transaction(db, transaction_id, current_user)