# 💰 Finance Tracker API

A Python-based Finance Tracking System built with **FastAPI**, **SQLite**, and **SQLAlchemy**.  
This project was built as part of a Python Developer Internship assessment.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Auth | JWT (JSON Web Tokens) |
| Validation | Pydantic |
| Server | Uvicorn |

---

## 📁 Project Structure

```
finance-tracker-api/
├── app/
│   ├── main.py                  # App entry point
│   ├── database.py              # Database connection and session
│   ├── models/
│   │   ├── user.py              # User table definition
│   │   └── transaction.py      # Transaction table definition
│   ├── routes/
│   │   ├── auth.py              # Register and login endpoints
│   │   ├── transactions.py     # CRUD endpoints for transactions
│   │   └── analytics.py        # Summary and analytics endpoints
│   ├── schemas/
│   │   ├── user.py              # Pydantic schemas for user input/output
│   │   └── transaction.py      # Pydantic schemas for transaction input/output
│   └── services/
│       ├── auth_service.py      # Auth business logic (hashing, JWT)
│       ├── transaction_service.py  # Transaction business logic
│       └── analytics_service.py   # Analytics and summary logic
├── .env                         # Environment variables (secret keys etc.)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker-api.git
cd finance-tracker-api
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./finance.db
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

### 6. Open API Docs
Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👥 User Roles

| Role | Permissions |
|---|---|
| **Viewer** | View transactions and summaries |
| **Analyst** | View + filter + detailed insights |
| **Admin** | Full access — create, update, delete records and users |

---

## 📌 API Overview

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |

### Transactions
| Method | Endpoint | Description |
|---|---|---|
| GET | `/transactions` | List all transactions (with filters) |
| POST | `/transactions` | Create a new transaction |
| PUT | `/transactions/{id}` | Update a transaction |
| DELETE | `/transactions/{id}` | Delete a transaction |

### Analytics
| Method | Endpoint | Description |
|---|---|---|
| GET | `/analytics/summary` | Total income, expenses, balance |
| GET | `/analytics/by-category` | Breakdown by category |
| GET | `/analytics/monthly` | Monthly totals |
| GET | `/analytics/recent` | Recent transactions |

---

## 🧪 Testing the API

You can test all endpoints directly via the **interactive Swagger UI**:
```
http://localhost:8000/docs
```

Or use **Postman** or **curl** for manual testing.

---

## 📝 Assumptions Made

- SQLite is used for simplicity; can be swapped with PostgreSQL easily
- JWT tokens are used for stateless authentication
- All amounts are stored as float values
- Dates are stored in ISO format (YYYY-MM-DD)
- Admin is the only role that can delete or modify records
- Seed data can be added via the `/auth/register` endpoint

---

## 🚧 Current Status

- [x] Project structure set up
- [ ] Database models defined
- [ ] Auth system (register + login + JWT)
- [ ] Transaction CRUD APIs
- [ ] Analytics APIs
- [ ] Validation and error handling
- [ ] Final testing and documentation

---

## 👨‍💻 Author

Built with ❤️ for the Zorvyn Python Developer Internship Assessment.