import pytest
from unittest.mock import MagicMock, patch
from modules.connector.product_manager import ProductCRUD, Product


@pytest.fixture
def mock_db():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    crud = ProductCRUD(mock_connection)

    yield crud, mock_cursor, mock_connection


class TestProductCRUD:

    def test_create_product(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        product = Product(name='Test Product',
                          description='Test Description',
                          price=10.00,
                          category_id="1",
                          supplier_id="1",
                          )

        crud.create_product(product.name, product.description, product.price, product.category_id, product.supplier_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_read_product(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        product_id = 1
        crud.read_product(product_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_update_product(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        product_id = 1
        product = Product(name='Updated Product')
        crud.update_product(product_id, product_name=product.name)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_delete_product(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        product_id = 1
        crud.delete_product(product_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_close(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        crud.close()

        # Check if the close methods were called on the mock cursor and connection
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

# To run the tests, you can use the command: pytest <filename>.py
