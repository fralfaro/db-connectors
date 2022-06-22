# -*- coding: utf-8 -*-
"""
.. autofunction:: azsql_connection
.. autofunction:: azsql_engine

"""
import os
from pyodbc import Connection, connect

def azsql_connection(
        host: str,
        database: str,
        user: str,
        password: str,
        authentication: str,
        driver =str
) -> Connection:
    """
    AZSQL connection

    :param host: host name
    :param database: database name
    :param user: user name
    :param password: password
    :param authentication: authentication
    :return: azsql connection
    """

    conn_string = f'''DRIVER={driver};
                                SERVER={host};
                                DATABASE={database};
                                UID={user};
                                PWD={password};
                                Authentication={authentication};'''
    conn = connect(conn_string)

    return conn

def azsql_engine():
    """
    Engine for AZSQL

    :return: engines
    """

    engine = azsql_connection(
        host = os.environ["AZSQL_HOST"],
        database = os.environ["AZSQL_NAME"],
        user = os.environ["AZSQL_USERNAME"],
        password = os.environ["AZSQL_PASSWORD"],
        authentication = os.environ["AZSQL_AUTHENTICATION"],
        driver=os.environ["DRIVER_SQL"]
    )

    return engine