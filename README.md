# 💰 Finance Tracker API

A Python-based Finance Tracking System built with FastAPI, SQLite, and SQLAlchemy.
Built as part of the Zorvyn Python Developer Internship Assessment.

---

 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Auth | JWT (JSON Web Tokens) |
| Validation | Pydantic |
| Server | Uvicorn |
| Password Hashing | Bcrypt (passlib) |

---

 📁 Project Structure


finance-tracker-api/
├── app/
│   ├── main.py                      # App entry point, route registration
│   ├── database.py                  # Database connection and session
│   ├── models/
│   │   ├── user.py                  # User table (id, name, email, role)
│   │   └── transaction.py          # Transaction table (amount, type, category, date)
│   ├── routes/
│   │   ├── auth.py                  # Register, login, /me endpoints
│   │   ├── transactions.py         # CRUD endpoints for transactions
│   │   └── analytics.py            # Summary and analytics endpoints
│   ├── schemas/
│   │   ├── user.py                  # Pydantic schemas for user input/output
│   │   └── transaction.py          # Pydantic schemas for transaction input/output
│   └── services/
│       ├── auth_service.py          # JWT creation, password hashing, role guard
│       ├── transaction_service.py  # Transaction business logic
│       └── analytics_service.py   # Analytics and summary logic
├── .env                             # Environment variables
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation


---

 ⚙️ Setup Instructions

# 1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/finance-tracker-api.git
cd finance-tracker-api


# 2. Create and Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux


# 3. Install Dependencies
bash
pip install -r requirements.txt


# 4. Configure Environment Variables
Create a `.env` file in the root directory:

SECRET_KEY=zorvyn_finance_super_secret_key_2024
DATABASE_URL=sqlite:///./finance.db
ACCESS_TOKEN_EXPIRE_MINUTES=30


# 5. Run the Application
bash
uvicorn app.main:app --reload


# 6. Open API Docs
Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

 👥 User Roles

| Role | Permissions |
|---|---|
| Viewer | View transactions and summaries, recent activity |
| Analyst | View + filter + category breakdown + monthly totals |
| Admin | Full access — create, update, delete records and users |

---

 📌 API Reference

# 🔐 Auth Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/auth/register` | None | Register a new user |
| POST | `/auth/login` | None | Login and get JWT token |
| GET | `/auth/me` | Any role | Get current user info |

# 💳 Transaction Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/transactions/` | Admin | Create a new transaction |
| GET | `/transactions/` | Any role | List all transactions (with filters) |
| GET | `/transactions/{id}` | Any role | Get single transaction |
| PUT | `/transactions/{id}` | Admin | Update a transaction |
| DELETE | `/transactions/{id}` | Admin | Delete a transaction |

 📊 Analytics Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/analytics/summary` | Any role | Total income, expenses, balance |
| GET | `/analytics/by-category` | Analyst, Admin | Breakdown by category |
| GET | `/analytics/monthly` | Analyst, Admin | Monthly income vs expenses |
| GET | `/analytics/recent` | Any role | Recent transactions |

---

 🧪 Testing the API

 Step 1 — Register a User
bash
curl -X POST "http://localhost:8000/auth/register" -H "Content-Type: application/json" -d "{\"name\": \"Admin User\", \"email\": \"admin@finance.com\", \"password\": \"admin123\", \"role\": \"admin\"}"


 Step 2 — Login and Get Token
bash
curl -X POST "http://localhost:8000/auth/login" -H "Content-Type: application/json" -d "{\"email\": \"admin@finance.com\", \"password\": \"admin123\"}"


 Step 3 — Use Token in Requests
bash
curl -X GET "http://localhost:8000/analytics/summary" -H "Authorization: Bearer YOUR_TOKEN_HERE"


 Step 4 — Create a Transaction
bash
curl -X POST "http://localhost:8000/transactions/" -H "Authorization: Bearer YOUR_TOKEN_HERE" -H "Content-Type: application/json" -d "{\"amount\": 50000, \"type\": \"income\", \"category\": \"Salary\", \"date\": \"2024-04-01\", \"notes\": \"Monthly salary\"}"


 Step 5 — Filter Transactions
bash
curl -X GET "http://localhost:8000/transactions/?transaction_type=income" -H "Authorization: Bearer YOUR_TOKEN_HERE"
curl -X GET "http://localhost:8000/transactions/?category=Food" -H "Authorization: Bearer YOUR_TOKEN_HERE"
curl -X GET "http://localhost:8000/transactions/?start_date=2024-04-01&end_date=2024-04-30" -H "Authorization: Bearer YOUR_TOKEN_HERE"


---

 🔍 Sample API Responses

 Summary Response
json
{
  "total_income": 70000.0,
  "total_expenses": 20000.0,
  "balance": 50000.0
}


 Category Breakdown Response
json
[
  {"category": "Salary", "type": "income", "total": 50000.0},
  {"category": "Freelance", "type": "income", "total": 20000.0},
  {"category": "Rent", "type": "expense", "total": 15000.0},
  {"category": "Food", "type": "expense", "total": 3000.0},
  {"category": "Transport", "type": "expense", "total": 2000.0}
]


 Monthly Totals Response
json
[
  {
    "month": "2024-04",
    "income": 70000.0,
    "expenses": 20000.0,
    "balance": 50000.0
  }
]


---

 ✅ Validation and Error Handling

| Scenario | Response |
|---|---|
| Duplicate email on register | `400 Bad Request` |
| Password less than 6 chars | `400 Bad Request` |
| Wrong email or password | `401 Unauthorized` |
| Missing or expired token | `401 Unauthorized` |
| Insufficient role | `403 Forbidden` |
| Transaction not found | `404 Not Found` |
| Negative amount | `422 Unprocessable Entity` |
| Empty category | `422 Unprocessable Entity` |

---

 📝 Assumptions Made

- SQLite is used for simplicity; can be swapped with PostgreSQL by changing `DATABASE_URL`
- JWT tokens are used for stateless authentication with 30 minute expiry
- All amounts are stored as float values in the database
- Dates follow ISO format `YYYY-MM-DD`
- Admin is the only role that can create, update, or delete transactions
- Analyst and Admin can access detailed analytics (category breakdown, monthly totals)
- All roles can view transactions, summaries, and recent activity
- Passwords are hashed using bcrypt before storage — never stored as plain text

---

🚀 Features Implemented

 User registration and login
 JWT based authentication
 Role based access control (Viewer, Analyst, Admin)
 Create, Read, Update, Delete transactions
 Filter transactions by type, category, and date range
 Financial summary (income, expenses, balance)
 Category wise breakdown
 Monthly totals with balance
 Recent transactions
 Input validation and error handling
 Clean project structure with separation of concerns
 Auto-generated API documentation via Swagger UI

---

 👨‍💻 Author

Built with ❤️ for the Zorvyn Python Developer Internship Assessment.