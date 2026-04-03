from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.transaction import TransactionResponse
from app.services.analytics_service import (
    get_summary,
    get_category_breakdown,
    get_monthly_totals,
    get_recent_transactions
)
from app.services.auth_service import get_current_user, require_role
from typing import List

router = APIRouter(prefix="/analytics", tags=["Analytics"])


# ─── Summary (All roles) ──────────────────────────────────────────

@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get total income, expenses and balance"""
    return get_summary(db)


# ─── Category Breakdown (Analyst + Admin) ────────────────────────

@router.get("/by-category")
def by_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_role(UserRole.analyst, UserRole.admin)
    )
):
    """Get breakdown of transactions by category"""
    return get_category_breakdown(db)


# ─── Monthly Totals (Analyst + Admin) ────────────────────────────

@router.get("/monthly")
def monthly(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_role(UserRole.analyst, UserRole.admin)
    )
):
    """Get income and expenses grouped by month"""
    return get_monthly_totals(db)


# ─── Recent Transactions (All roles) ─────────────────────────────

@router.get("/recent", response_model=List[TransactionResponse])
def recent(
    limit: int = Query(default=5, ge=1, le=20),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get most recent transactions"""
    return get_recent_transactions(db, limit)