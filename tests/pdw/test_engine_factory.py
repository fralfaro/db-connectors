import pytest

from db_connectors.pdw import pdw_engine


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv("PDW_HOST", "host")
    monkeypatch.setenv("PDW_PORT", "port")
    monkeypatch.setenv("PDW_DATABASE", "database")
    monkeypatch.setenv("PDW_USERNAME", "user")
    monkeypatch.setenv("PDW_PASSWORD", "password")
    monkeypatch.setenv("DRIVER_SQL", "driver")


def test_engine_factory(mocker):
    pdw = mocker.patch("db_connectors.pdw.pdw_connection")
    engine = pdw_engine()

    pdw.assert_called_once_with(
        host="host",
        port="port",
        database="database",
        user="user",
        password="password",
        driver="driver",
    )

    assert engine == pdw.return_value
