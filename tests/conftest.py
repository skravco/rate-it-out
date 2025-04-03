import os
import pytest
from unittest.mock import patch
from app import app, init_db

@pytest.fixture
def client():
    """Fixture to create a test client."""
    with patch("app.send_mail") as mock_send_mail:  # Mock the send_mail function
        os.environ['DATABASE'] = 'test_feedback.db'
        mock_send_mail.return_value = None  # Prevents actual email sending
        with app.test_client() as client:
            with app.app_context():
                init_db()  # Initialize test database
            yield client
        os.remove('test_feedback.db')  # Cleanup after tests
