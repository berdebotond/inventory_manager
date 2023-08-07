import dataclasses


@dataclasses.dataclass
class Category:
    name: str = None
    description: str = None


class CategoryCRUD:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_category(self, category_name, description):
        try:
            sql = """
                INSERT INTO Categories (category_name, description)
                VALUES (%s, %s) RETURNING category_id;
            """
            self.cursor.execute(sql, (category_name, description))
            self.connection.commit()
            return self.cursor.fetchone()[0]  # Return the generated category_id
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating category: {e}")
            return None

    def read_category(self, category_id):
        try:
            sql = "SELECT * FROM Categories WHERE category_id = %s;"
            self.cursor.execute(sql, (category_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error reading category: {e}")
            return None

    def update_category(self, category_id, category_name=None, description=None):
        try:
            updates = []
            values = []

            if category_name:
                updates.append("category_name = %s")
                values.append(category_name)
            if description:
                updates.append("description = %s")
                values.append(description)

            values.append(category_id)

            sql = "UPDATE Categories SET " + ", ".join(updates) + " WHERE category_id = %s;"
            self.cursor.execute(sql, tuple(values))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating category: {e}")

    def delete_category(self, category_id):
        try:
            sql = "DELETE FROM Categories WHERE category_id = %s;"
            self.cursor.execute(sql, (category_id,))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting category: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
