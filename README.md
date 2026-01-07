# 🚗 Premium Auto Showroom

A full-featured, production-ready Flask application for managing and displaying a vehicle showroom. This application features a sleek, responsive design, a robust administrative backend, and an inquiry system for potential buyers.

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563d7c.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## ✨ Features

- **Inventory Showcase**: Stylish grid view of available vehicles with high-quality image support.
- **Advanced Filtering**: Filter inventory by Make, Price Range, and availability.
- **Detailed Vehicle Pages**: Comprehensive view of vehicle specifications, descriptions, and dynamic price formatting.
- **Customer Inquiry System**: Integrated contact forms for specific vehicles with database logging.
- **Admin Dashboard**: Secure management interface for CRUD operations (Create, Read, Update, Delete) on vehicles.
- **Image Processing**: Automatic image handling and validation for vehicle uploads.
- **Custom Error Handling**: Polished 404 and 500 error pages for a seamless user experience.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, Vanilla CSS3, JavaScript (ES6+), Bootstrap 5
- **Forms**: Flask-WTF (WTForms)
- **Migrations**: Flask-Migrate (Alembic)
- **Image Handling**: Pillow

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/vehicle-showroom.git
   cd vehicle-showroom
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database and sample data**
   ```bash
   python create_sample_data.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```
   Visit `http://localhost:5000` in your browser.

## 📂 Project Structure

```text
vehicle-showroom/
├── app/
│   ├── errors/          # Custom error handlers
│   ├── static/          # CSS, JS, and Image uploads
│   ├── templates/       # Jinja2 HTML templates
│   ├── forms.py         # WTForms definitions
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes (Main & Admin)
│   └── utils.py         # Image processing utilities
├── config.py            # Environment configuration
├── run.py               # Development entry point
├── wsgi.py              # Production entry point
└── requirements.txt     # Python dependencies
```

## 🔒 Security

For production deployments:
- Set `FLASK_ENV=production` in your `.env`.
- Change the `SECRET_KEY` to a secure, random string.
- Use `gunicorn` or a similar WSGI server (included in requirements).

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Created with ❤️ by Antigravity AI
