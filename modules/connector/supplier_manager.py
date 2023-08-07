import dataclasses


@dataclasses.dataclass
class Supplier:
    name: str = None
    contact_name: str = None
    contact_email: str = None
    contact_phone: str = None


class SupplierCRUD:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_supplier(self, supplier_name, contact_name, contact_email, contact_phone):
        try:
            sql = """
                INSERT INTO Suppliers (supplier_name, contact_name, contact_email, contact_phone)
                VALUES (%s, %s, %s, %s) RETURNING supplier_id;
            """
            self.cursor.execute(sql, (supplier_name, contact_name, contact_email, contact_phone))
            self.connection.commit()
            return self.cursor.fetchone()[0]  # Return the generated supplier_id
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating supplier: {e}")
            return None

    def read_supplier(self, supplier_id):
        try:
            sql = "SELECT * FROM Suppliers WHERE supplier_id = %s;"
            self.cursor.execute(sql, (supplier_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error reading supplier: {e}")
            return None

    def update_supplier(self, supplier_id, supplier_name=None, contact_name=None, contact_email=None,
                        contact_phone=None):
        try:
            updates = []
            values = []

            if supplier_name:
                updates.append("supplier_name = %s")
                values.append(supplier_name)
            if contact_name:
                updates.append("contact_name = %s")
                values.append(contact_name)
            if contact_email:
                updates.append("contact_email = %s")
                values.append(contact_email)
            if contact_phone:
                updates.append("contact_phone = %s")
                values.append(contact_phone)

            values.append(supplier_id)

            sql = "UPDATE Suppliers SET " + ", ".join(updates) + " WHERE supplier_id = %s;"
            self.cursor.execute(sql, tuple(values))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating supplier: {e}")

    def delete_supplier(self, supplier_id):
        try:
            sql = "DELETE FROM Suppliers WHERE supplier_id = %s;"
            self.cursor.execute(sql, (supplier_id,))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting supplier: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
