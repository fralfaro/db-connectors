from db_connectors.azsql import azsql_connection


def test_connection(mocker):

    host = 'host',
    database = 'database'
    user = 'user',
    password = 'password'
    authentication = 'authentication'
    driver = 'driver'

    connect = mocker.patch(
        "db_connectors.azsql.connect"
    )  # sin cambios

    expected_str = f'''DRIVER={driver};
                                SERVER={host};
                                DATABASE={database};
                                UID={user};
                                PWD={password};
                                Authentication={authentication};'''
    azsql_connection(
        host= host,
        database= database,
        user= user,
        password= password,
        authentication= authentication,
        driver= driver
        )

    connect.assert_called_once_with(expected_str)


