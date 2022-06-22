# -*- coding: utf-8 -*-
"""
.. autofunction:: ibm_connection
.. autofunction:: ibm_engine

"""
import os
import ibm_db_dbi as db
from ibm_db_dbi import Connection

def ibm_connection(
        host: str,
        port: str,
        database: str,
        user: str,
        password: str
)->Connection:
    """
    IBM connection

    :param host: host name
    :param port: port number
    :param database: database name
    :param user: user name
    :param password: password
    :return: pwd connection
    """

    conn = db.connect(
        f"DATABASE={database};HOSTNAME={host};PORT={port};PROTOCOL=TCPIP;UID={user};PWD={password};",
        "","","")


    return conn

def ibm_engine():
    """
    Engine for IBM

    :return: engines
    """

    engine = ibm_connection(
        host = os.environ["IBM_HOST"],
        port = os.environ["IBM_PORT"],
        database = os.environ["IBM_DATABASE"],
        user = os.environ["IBM_USERNAME"],
        password = os.environ["IBM_PASSWORD"],
    )

    return engine