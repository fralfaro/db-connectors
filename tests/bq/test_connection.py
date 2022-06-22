from db_connectors.bq import bq_connection


def test_connection(mocker):

    id_project = 'id_project'


    mock_client = mocker.patch('google.cloud.bigquery.Client', autospec=True)


    bq_connection(
        project_id= id_project,
       )


