import pytest
from unittest.mock import MagicMock, patch
from modules.connector.category_manager import CategoryCRUD, Category


@pytest.fixture
def mock_db():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    crud = CategoryCRUD(mock_connection)

    yield crud, mock_cursor, mock_connection


class TestCategoryCRUD:

    def test_create_category(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        category = Category(name='Sample Category', description='Sample Description')
        crud.create_category(category.name, category.description)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_read_category(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        category_id = 1
        crud.read_category(category_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_update_category(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        category_id = 1
        category = Category(name='Updated Category')
        crud.update_category(category_id, category_name=category.name)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_delete_category(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        category_id = 1
        crud.delete_category(category_id)

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_close(self, mock_db):
        crud, mock_cursor, mock_connection = mock_db
        crud.close()

        # Check if the close methods were called on the mock cursor and connection
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

# To run the tests, you can use the command: pytest <filename>.py
