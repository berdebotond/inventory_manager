import psycopg2
from modules.config.config import config


class InventoryDatabase:
    def __init__(self):
        self.connection = psycopg2.connect(
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            database=config.POSTGRES_DB
        )
        self.cursor = self.connection.cursor()

    def initialize(self):
        self.create_tables()
    def create_tables(self):
        # Create Suppliers table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Suppliers (
                supplier_id SERIAL PRIMARY KEY,
                supplier_name VARCHAR(255) NOT NULL,
                contact_name VARCHAR(255),
                contact_email VARCHAR(255),
                contact_phone VARCHAR(15)
            );
        ''')

        # Create Categories table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Categories (
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR(255) NOT NULL,
                description TEXT
            );
        ''')

        # Create Products table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2),
                category_id INTEGER REFERENCES Categories(category_id),
                supplier_id INTEGER REFERENCES Suppliers(supplier_id)
            );
        ''')

        # Create Inventory table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Inventory (
                inventory_id SERIAL PRIMARY KEY,
                product_id INTEGER REFERENCES Products(product_id),
                quantity_on_hand INTEGER NOT NULL,
                reorder_level INTEGER
            );
        ''')

        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

