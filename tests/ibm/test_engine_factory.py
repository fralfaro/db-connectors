import pytest

from db_connectors.ibm import ibm_engine


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv("IBM_USERNAME", "user")
    monkeypatch.setenv("IBM_PASSWORD", "password")
    monkeypatch.setenv("IBM_HOST", "host")
    monkeypatch.setenv("IBM_DATABASE", "database")
    monkeypatch.setenv("IBM_PORT", "port")


def test_engine_factory(mocker):
    pdw = mocker.patch("db_connectors.ibm.ibm_connection")
    engine = ibm_engine()

    pdw.assert_called_once_with(
        host="host",
        port="port",
        database="database",
        user="user",
        password="password",
    )

    assert engine == pdw.return_value
