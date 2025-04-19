import main
import os


def test_export_envs():
    main.export_envs("test")
    assert os.environ["API_KEY"] is not None
    assert os.environ["ENVIRONMENT"] == "test"
    assert os.environ["APP_NAME"] == "app-test"
