# 🏬 Ecom-Core-Django

A classic **Django-based eCommerce web application** built using Django's core features like templates, models, views, and the admin panel. This project serves as a clean foundation for building feature-rich, server-rendered eCommerce websites using **only Django** — no DRF or API frameworks involved.

---

## 🚀 Features

- 🛍️ Product catalog (Add/Edit/Delete from Admin)
- 🛒 Shopping cart functionality
- 👤 User authentication (Login, Logout, Register)
- 📦 Order placement & tracking logic (basic)
- 🧑‍💼 Admin panel for managing products, users, and orders
- 🎨 Server-rendered HTML using Django templates

---

## 📁 Project Structure

```
Ecom/
├── blog/             # blog app
├── E_Com/            # Main Project
  ├── settings.py/    # Congiguration
  ├── urls.py/        # URL's
  ├── static/         # Static files (CSS, JS, images)
├── media/            # media
├── shop/             # shop app
  ├── models.py/      # Models
  ├── urls.py/        # URL's
  ├── Views.py        # Views
└── manage.py
```

---

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/adityagirigoswami/Ecom-Core-Django.git
cd Ecom-Core-Django
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
python manage.py makemigrations

```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Now, open `http://127.0.0.1:8000/` in your browser to view the site.

---

## 🔐 Admin Panel

- Visit: `http://127.0.0.1:8000/admin/`
- Log in using your superuser credentials
- Add/manage products, orders, and users from here

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit pull requests.

1. Fork the project  
2. Create a feature branch (`git checkout -b feature/xyz`)  
3. Commit your changes (`git commit -m "Add xyz"`)  
4. Push to your branch (`git push origin feature/xyz`)  
5. Open a Pull Request

---

## 🙏 Acknowledgements

Developed by **Aditya Goswami** as part of learning and mastering Django's core framework.  
Inspired by traditional eCommerce architectures.

---
