import pytest
from db_connectors.bq import bq_engine


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv("ID_PROJECT", "id_project")


def test_engine_factory(mocker):
    bq = mocker.patch("db_connectors.bq.bq_connection")
    engine = bq_engine()

    bq.assert_called_once_with(
        project="id_project",
    )

    assert engine == bq.return_value
