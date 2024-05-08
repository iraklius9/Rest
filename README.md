# Django Product Management System

This project is a simple product management system built with Django.
### 1. Install dependencies: pip install -r requirements.txt
### 2. Set up the database: python manage.py migrate
### 3. Run the development server: python manage.py runserver

## Usage

- Access the Django admin interface to manage products and categories: [Admin Interface](http://localhost:8000/admin/) (login required)
- Use the provided API endpoints for CRUD operations on products:
- Product listing: [http://localhost:8000/api/products/](http://localhost:8000/api/products/)
- Product detail: [http://localhost:8000/api/products/<id>/](http://localhost:8000/api/products/<id>/)
- Create product: [http://localhost:8000/api/products/create/](http://localhost:8000/api/products/create/)
- Update product: [http://localhost:8000/api/products/<id>/update/](http://localhost:8000/api/products/<id>/update/)
- Delete product: [http://localhost:8000/api/products/<id>/delete/](http://localhost:8000/api/products/<id>/delete/)


