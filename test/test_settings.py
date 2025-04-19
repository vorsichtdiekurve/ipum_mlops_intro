from settings import Settings


def test_settings():
    settings = Settings()

    assert settings.APP_NAME == "app-test"
    assert settings.ENVIRONMENT == "test"
    assert settings.API_KEY is not None
