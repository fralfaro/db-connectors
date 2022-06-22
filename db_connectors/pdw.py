# -*- coding: utf-8 -*-
"""
.. autofunction:: pdw_connection
.. autofunction:: pdw_engine

"""
import os
from pyodbc import Connection, connect


def pdw_connection(
        host: str,
        port: str,
        database: str,
        user: str,
        password: str,
        driver:str
) -> Connection:
    """
    PDW connection

    :param host: host name
    :param port: port number
    :param database: database name
    :param user: user name
    :param password: password
    :return: pwd connection
    """

    #driver = '{ODBC Driver 17 for SQL Server}'
    conn_string = f'DRIVER={driver};SERVER={host},{port};DATABASE={database};UID={user};PWD={password}'

    conn = connect(conn_string)

    return conn

def pdw_engine():
    """
    Engine for PWD

    :return: engines
    """

    engine = pdw_connection(
        host = os.environ["PDW_HOST"],
        port = os.environ["PDW_PORT"],
        database = os.environ["PDW_DATABASE"],
        user = os.environ["PDW_USERNAME"],
        password = os.environ["PDW_PASSWORD"],
        driver = os.environ["DRIVER_SQL"]
    )

    return engine