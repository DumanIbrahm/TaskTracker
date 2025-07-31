import pytest
from app import create_app
from app.db import init_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'

    with app.app_context():
        init_db(app)  # Tablolar burada oluşturuluyor

    with app.test_client() as client:
        yield client
