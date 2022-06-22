import pytest

from db_connectors.azsql import azsql_engine


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv("AZSQL_USERNAME", "user")
    monkeypatch.setenv("AZSQL_PASSWORD", "password")
    monkeypatch.setenv("AZSQL_HOST", "host")
    monkeypatch.setenv("AZSQL_NAME", "database")
    monkeypatch.setenv("AZSQL_AUTHENTICATION", "authentication")
    monkeypatch.setenv("DRIVER_SQL", "driver")



def test_engine_factory(mocker):
    azsql = mocker.patch("db_connectors.azsql.azsql_connection")
    engine = azsql_engine()

    azsql.assert_called_once_with(
        host = 'host',
        database = 'database',
        user = 'user',
        password = 'password',
        authentication = 'authentication',
        driver = 'driver'
    )

    assert engine == azsql.return_value
