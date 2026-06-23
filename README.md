# 🛒 UrbanCart - E-Commerce Platform

> Full-stack e-commerce app built with **Python, Flask, SQLite, HTML, CSS, and Bootstrap 5**

## 🚀 Features
- 🛍️ Product catalog with category badges & hover effects
- 🛒 Shopping cart — add, remove, quantity tracking
- ✅ One-click checkout with order confirmation
- 📋 Complete order management & history
- 📱 Fully responsive across all devices

## 🛠️ Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3, Flask |
| Database | SQLite (raw SQL, no ORM) |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Icons | Bootstrap Icons |

## ⚙️ How to Run Locally
```bash
# 1. Install dependency
pip install flask

# 2. Run the app
python app.py

# 3. Open browser
http://127.0.0.1:5000
```

## 📁 Project Structure

UrbanCart/
├── app.py          → All Flask routes (6 routes)
├── database.py     → DB init, schema & product seeding
├── templates/
│   ├── base.html   → Shared navbar layout
│   ├── index.html  → Product catalog grid
│   ├── cart.html   → Cart table + checkout
│   └── orders.html → Order history
└── static/css/
└── style.css   → Custom design & animations

## 📸 Pages
| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Product catalog |
| Cart | `/cart` | Shopping cart |
| Orders | `/orders` | Order history |

## 👨‍💻 Author
**Rahul Madhan** — B.Tech CSE (AIML) | GATE CS 2026 Qualified
