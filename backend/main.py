from fastapi import FastAPI
from models import (
    UserCreate,
    AccountCreate,
    CategoryCreate,
    ExpenseCreate
)

app = FastAPI()

# -------------------
# System
# -------------------

@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------
# Users
# -------------------

@app.post("/users")
def create_user(user: UserCreate):
    return {"message": "User created (stub)"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}

# -------------------
# Accounts
# -------------------

@app.post("/accounts")
def create_account(account: AccountCreate):
    return {"message": "Account created (stub)"}

@app.get("/accounts/{user_id}")
def get_accounts(user_id: str):
    return {"user_id": user_id, "accounts": []}

# -------------------
# Categories
# -------------------

@app.post("/categories")
def create_category(category: CategoryCreate):
    return {"message": "Category created (stub)"}

@app.get("/categories/{user_id}")
def get_categories(user_id: str):
    return {"user_id": user_id, "categories": []}

# -------------------
# Expenses
# -------------------

@app.post("/expenses")
def create_expense(expense: ExpenseCreate):
    return {"message": "Expense created (stub)"}

@app.get("/expenses/{user_id}")
def get_expenses(user_id: str):
    return {"user_id": user_id, "expenses": []}

@app.get("/expenses/{user_id}/{account_id}")
def get_expenses_by_account(user_id: str, account_id: str):
    return {"user_id": user_id, "account_id": account_id, "expenses": []}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: str):
    return {"message": f"Expense {expense_id} deleted (stub)"}
