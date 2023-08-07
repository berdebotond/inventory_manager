
# Inventory Management System

An inventory management system built using Python and PostgreSQL. This system allows users to manage products, suppliers, and categories in an organized manner.

## Features

- CRUD operations for Products, Suppliers, and Categories.
- Error handling for database operations.
- Unit tests for ensuring the reliability of the system.

## Prerequisites

- Python 3.x
- PostgreSQL
- psycopg2

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd path-to-directory
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and update the configuration in `config.py`.

## Usage

1. Initialize the database tables:
   ```python
   from modules.connector.Inventory_manager import InventoryDatabase
   db = InventoryDatabase()
   ```

2. Use the CRUD classes for managing Products, Suppliers, and Categories:
   ```python
   from your_module import ProductCRUD, SupplierCRUD, CategoryCRUD
   product_crud = ProductCRUD(connection)
   supplier_crud = SupplierCRUD(connection)
   category_crud = CategoryCRUD(connection)
   ```

3. Run the unit tests to ensure everything is working as expected:
   ```
   pytest test_filename.py
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

You can copy the above content and paste it directly into your `README.md` file. Make sure to replace placeholders like `<repository-url>` and `path-to-directory` with the actual values relevant to your project.