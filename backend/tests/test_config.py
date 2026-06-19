from app.config import Settings


def test_normalize_railway_postgres_url():
    settings = Settings(database_url="postgres://user:pass@host:5432/railway")
    assert settings.database_url == "postgresql://user:pass@host:5432/railway"


def test_sqlite_url_unchanged():
    settings = Settings(database_url="sqlite:///./data/rupee_radar.db")
    assert settings.database_url == "sqlite:///./data/rupee_radar.db"
