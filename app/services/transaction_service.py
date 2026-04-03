from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException, status
from app.models.transaction import Transaction, TransactionType
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.models.user import User
from datetime import date
from typing import Optional


def create_transaction(
    db: Session,
    data: TransactionCreate,
    current_user: User
) -> Transaction:
    """Create a new transaction for the current user"""

    new_transaction = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        notes=data.notes,
        user_id=current_user.id
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


def get_all_transactions(
    db: Session,
    current_user: User,
    transaction_type: Optional[TransactionType] = None,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> list[Transaction]:
    """Get all transactions with optional filters"""

    # Start with base query
    query = db.query(Transaction)

    # Filter by type if provided
    if transaction_type:
        query = query.filter(Transaction.type == transaction_type)

    # Filter by category if provided
    if category:
        query = query.filter(
            Transaction.category.ilike(f"%{category}%")
        )

    # Filter by date range if provided
    if start_date:
        query = query.filter(Transaction.date >= start_date)

    if end_date:
        query = query.filter(Transaction.date <= end_date)

    # Order by most recent first
    return query.order_by(Transaction.date.desc()).all()


def get_transaction_by_id(
    db: Session,
    transaction_id: int
) -> Transaction:
    """Get a single transaction by ID"""

    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transaction_id} not found"
        )

    return transaction


def update_transaction(
    db: Session,
    transaction_id: int,
    data: TransactionUpdate,
    current_user: User
) -> Transaction:
    """Update an existing transaction"""

    transaction = get_transaction_by_id(db, transaction_id)

    # Only update fields that were actually provided
    if data.amount is not None:
        transaction.amount = data.amount
    if data.type is not None:
        transaction.type = data.type
    if data.category is not None:
        transaction.category = data.category
    if data.date is not None:
        transaction.date = data.date
    if data.notes is not None:
        transaction.notes = data.notes

    db.commit()
    db.refresh(transaction)

    return transaction


def delete_transaction(
    db: Session,
    transaction_id: int,
    current_user: User
) -> dict:
    """Delete a transaction"""

    transaction = get_transaction_by_id(db, transaction_id)

    db.delete(transaction)
    db.commit()

    return {"message": f"Transaction {transaction_id} deleted successfully"}