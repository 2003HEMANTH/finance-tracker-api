from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction, TransactionType


def get_summary(db: Session) -> dict:
    """Total income, expenses and current balance"""

    total_income = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.type == TransactionType.income
    ).scalar() or 0

    total_expenses = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.type == TransactionType.expense
    ).scalar() or 0

    balance = total_income - total_expenses

    return {
        "total_income": round(total_income, 2),
        "total_expenses": round(total_expenses, 2),
        "balance": round(balance, 2)
    }


def get_category_breakdown(db: Session) -> list:
    """Total amount spent/earned per category"""

    results = db.query(
        Transaction.category,
        Transaction.type,
        func.sum(Transaction.amount).label("total")
    ).group_by(
        Transaction.category,
        Transaction.type
    ).all()

    breakdown = []
    for row in results:
        breakdown.append({
            "category": row.category,
            "type": row.type,
            "total": round(row.total, 2)
        })

    return breakdown


def get_monthly_totals(db: Session) -> list:
    """Income and expenses grouped by month"""

    results = db.query(
        extract("year", Transaction.date).label("year"),
        extract("month", Transaction.date).label("month"),
        Transaction.type,
        func.sum(Transaction.amount).label("total")
    ).group_by(
        "year",
        "month",
        Transaction.type
    ).order_by(
        "year",
        "month"
    ).all()

    # Organize into a clean structure
    monthly = {}
    for row in results:
        key = f"{int(row.year)}-{int(row.month):02d}"
        if key not in monthly:
            monthly[key] = {
                "month": key,
                "income": 0,
                "expenses": 0
            }
        if row.type == TransactionType.income:
            monthly[key]["income"] = round(row.total, 2)
        else:
            monthly[key]["expenses"] = round(row.total, 2)

    # Add balance to each month
    for key in monthly:
        monthly[key]["balance"] = round(
            monthly[key]["income"] - monthly[key]["expenses"], 2
        )

    return list(monthly.values())


def get_recent_transactions(db: Session, limit: int = 5) -> list:
    """Get most recent transactions"""

    results = db.query(Transaction).order_by(
        Transaction.date.desc()
    ).limit(limit).all()

    return results