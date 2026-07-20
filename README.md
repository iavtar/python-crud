# Inventory Management System (Python + MySQL)

A simple CRUD (Create, Read, Update, Delete) application built using **Python** and **MySQL** following a layered architecture (DAO + Service + Model).

## Project Structure

```
inventory_management/
│
├── main.py
│
├── config/
│   └── db.py
│
├── model/
│   └── product.py
│
├── dao/
│   └── product_dao.py
│
└── service/
    └── product_service.py
```

---

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Workbench (Optional)

---

## Database Setup

### Create Database

```sql
CREATE DATABASE inventory;
```

### Use Database

```sql
USE inventory;
```

### Create Table

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT
);
```

---

## Install Dependencies

Install all required Python packages:

```bash
python -m pip install -r requirements.txt
```

### requirements.txt

```text
mysql-connector-python==9.4.0
```

---

## Configure Database Connection

Update the database credentials in:

```
config/db.py
```

Example:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="inventory"
    )
```

---

## Run the Application

```bash
python main.py
```

---

## Features

- Add Product
- View All Products
- Find Product by ID
- Update Product
- Delete Product

---

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python

---

## Architecture

```
main.py
    │
    ▼
ProductService
    │
    ▼
ProductDAO
    │
    ▼
MySQL Database
```

---

## CRUD Operations

| Operation | Description |
|-----------|-------------|
| Create | Add a new product |
| Read | Retrieve one or all products |
| Update | Modify existing product details |
| Delete | Remove a product |

---

## Author: Indra Avatar Singh

Built as part of a Python + MySQL learning project following a layered architecture (Model → DAO → Service).