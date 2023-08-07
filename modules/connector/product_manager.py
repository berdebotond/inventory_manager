import dataclasses


class Product:
    name: str = None
    description: str = None
    price: float = None
    category_id = str
    supplier_id = str

    def __init__(self,
                 name: str,
                 price: float = 0.0,
                 description: str = "",
                 category_id: str = "",
                 supplier_id: str = "",
                 ):

        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.supplier_id = supplier_id


class ProductCRUD:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_product(self, product_name, description, price, category_id, supplier_id):
        try:
            sql = """
                INSERT INTO Products (product_name, description, price, category_id, supplier_id)
                VALUES (%s, %s, %s, %s, %s) RETURNING product_id;
            """
            self.cursor.execute(sql, (product_name, description, price, category_id, supplier_id))
            self.connection.commit()
            return self.cursor.fetchone()[0]  # Return the generated product_id
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating product: {e}")
            return None

    def read_product(self, product_id):
        try:
            sql = "SELECT * FROM Products WHERE product_id = %s;"
            self.cursor.execute(sql, (product_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error reading product: {e}")
            return None

    def update_product(self, product_id, product_name=None, description=None, price=None, category_id=None,
                       supplier_id=None):
        try:
            updates = []
            values = []

            if product_name:
                updates.append("product_name = %s")
                values.append(product_name)
            if description:
                updates.append("description = %s")
                values.append(description)
            if price:
                updates.append("price = %s")
                values.append(price)
            if category_id:
                updates.append("category_id = %s")
                values.append(category_id)
            if supplier_id:
                updates.append("supplier_id = %s")
                values.append(supplier_id)

            values.append(product_id)

            sql = "UPDATE Products SET " + ", ".join(updates) + " WHERE product_id = %s;"
            self.cursor.execute(sql, tuple(values))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating product: {e}")

    def delete_product(self, product_id):
        try:
            sql = "DELETE FROM Products WHERE product_id = %s;"
            self.cursor.execute(sql, (product_id,))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting product: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
