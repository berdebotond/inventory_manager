import pytest
from unittest.mock import MagicMock, patch
from modules.connector.Inventory_manager import InventoryDatabase
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_db():
    with patch('psycopg2.connect') as mock_connect:
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        db = InventoryDatabase()

        yield db, mock_cursor, mock_connection


@pytest.fixture
def mock_db():
    with patch('psycopg2.connect') as mock_connect:
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        db = InventoryDatabase()

        yield db, mock_cursor, mock_connection


class TestInventoryDatabase:

    def test_create_tables(self, mock_db):
        db, mock_cursor, mock_connection = mock_db
        db.create_tables()  # Explicitly call the create_tables method here

        # Check if the SQL commands were executed on the mock cursor
        assert mock_cursor.execute.called

    def test_close(self, mock_db):
        db, mock_cursor, mock_connection = mock_db
        db.close()
        # Check if the close methods were called on the mock cursor and connection
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

# To run the tests, you can use the command: pytest <filename>.py
