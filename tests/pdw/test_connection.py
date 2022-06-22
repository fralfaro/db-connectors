from db_connectors.pdw import pdw_connection


def test_connection(mocker):


    host = 'host'
    port = 'port'
    database = 'database'
    user = 'user'
    password = 'password'
    driver = 'driver'

    connect = mocker.patch(
        "db_connectors.pdw.connect"
    )  # sin cambios

    expected_str = f'DRIVER={driver};SERVER={host},{port};DATABASE={database};UID={user};PWD={password}'

    pdw_connection(
        host = host,
        port = port,
        database = database,
        user = user,
        password = password,
        driver = driver
    )

    connect.assert_called_once_with(expected_str)


