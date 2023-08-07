import pytest
from unittest.mock import MagicMock, patch
from modules.connector.supplier_manager import SupplierCRUD, Supplier


@pytest.fixture
def mock_db():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    crud = SupplierCRUD(mock_connection)

    yield crud, mock_cursor, mock_connection


class TestSupplierCRUD:

    def test_create_supplier(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        supplier = Supplier(name='Sample Supplier', contact_name='John Doe', contact_email='john@example.com',
                            contact_phone='1234567890')
        crud.create_supplier(supplier.name, supplier.contact_name, supplier.contact_email, supplier.contact_phone)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_read_supplier(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        supplier_id = 1
        crud.read_supplier(supplier_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_update_supplier(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        supplier_id = 1
        supplier = Supplier(name='Updated Supplier')
        crud.update_supplier(supplier_id, supplier_name=supplier.name)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_delete_supplier(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        supplier_id = 1
        crud.delete_supplier(supplier_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_close(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        crud.close()

        # Check if the close methods were called on the mock cursor and connection
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

# To run the tests, you can use the command: pytest <filename>.py
