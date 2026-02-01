from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: str
    name: str


class User(UserCreate):
    user_id: str
    created_at: datetime


class AccountCreate(BaseModel):
    user_id: str
    name: str
    type: str   # personal or business


class Account(AccountCreate):
    account_id: str
    created_at: datetime


class CategoryCreate(BaseModel):
    user_id: str
    name: str


class Category(CategoryCreate):
    category_id: str


class ExpenseCreate(BaseModel):
    user_id: str
    account_id: str
    category_id: str
    amount: float
    description: Optional[str] = None
    expense_date: datetime


class Expense(ExpenseCreate):
    expense_id: str
    created_at: datetime
