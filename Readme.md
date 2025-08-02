# Brilliant - Multi-Branch Bike Dealer Web App

This project is a microservices-based Django web application designed for a multi-branch bike dealer.

## ✅ Features (Implemented So Far)

- **Authentication Microservice**:
  - User Registration (`/register/`)
  - User Login (`/login/`)
  - Dashboard view (`/dashboard/`)
  - Logout functionality (`/logout/`)
  - TailwindCSS v3.4 styling
  - Responsive UI with secure login
  
## 🔧 Tech Stack

- Django 5.2.4
- Python 3.12+
- Tailwind CSS 3.4
- HTML Templates
- Git + GitHub

## 📁 Microservice Architecture

- `auth_service/` – Handles registration, login, logout, and dashboard
- `booking_service/` – Coming next (bike service appointments)

## 🛠️ Setup Instructions

```bash
git clone https://github.com/iseosethu/brilliant.git
cd brilliant
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
