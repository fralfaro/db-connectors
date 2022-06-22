# -*- coding: utf-8 -*-
"""
.. autofunction:: bq_connection
.. autofunction:: bq_engine

"""
from google.cloud import bigquery
from google.cloud.bigquery import Client
import os


def bq_connection(
        project_id: str,
) -> Client:
    """
    BigQuery connection

    :param project_id: project id
    :return: BigQuery connection
    """

    conn  = bigquery.Client(
        project=project_id,
    )


    return conn

def bq_engine():
    """
    Engine for BigQuery

    :return: engines
    """

    engine = bq_connection(
        project= os.environ["ID_PROJECT"]
    )

    return engine



