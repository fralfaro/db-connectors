from db_connectors.ibm import ibm_connection


def test_connection(mocker):

    host = "host"
    port = "port"
    database = "database"
    user = "user"
    password = "password"

    connect = mocker.patch("db_connectors.ibm.db")

    ibm_connection(
        host=host, port=port, database=database, user=user, password=password
    )
