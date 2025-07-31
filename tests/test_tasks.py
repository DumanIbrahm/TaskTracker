import pytest
from app import create_app
from app.db import init_db

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    app = create_app()
    app.config['TESTING'] = True
    app.config['DATABASE'] = str(db_path)

    with app.app_context():
        init_db(app)  # tablo burada dosya bazlı DB'de oluşturuluyor

    with app.test_client() as client:
        yield client
