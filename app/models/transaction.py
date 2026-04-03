from sqlalchemy import Column, Integer, Float, String, Enum, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
import enum


# Only two types of transactions allowed
class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    # The money amount — e.g. 5000.00
    amount = Column(Float, nullable=False)

    # Income or expense
    type = Column(Enum(TransactionType), nullable=False)

    # e.g. Salary, Food, Rent, Transport
    category = Column(String, nullable=False)

    # When this transaction happened
    date = Column(Date, nullable=False)

    # Optional extra info
    notes = Column(Text, nullable=True)

    # Which user created this transaction
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # This lets us do transaction.user to get the user object
    user = relationship("User", backref="transactions")