Introduction
=============


Description
-----------


The main goal is use the same repository to connect data and use same enviroment variables.
The connectors that we have are: **PDW**, **IBM**, **AZSQL** and **BIG QUERY**.

Getting Started
---------------

You need to setup a new env with python 3.8+ and some environment variables.


Prerequisites
-------------

You need a file named ``.env`` on root of the project, this file look like this:

.. code-block::

    PDW_USERNAME=<host>
    PDW_PASSWORD=<password>
    PDW_HOST=<host>
    PDW_DATABASE=<name>
    PDW_PORT=<port>
    PDW_NAME=<username>

    AZSQL_HOST=<host>
    AZSQL_NAME=<name>
    AZSQL_USERNAME=<username>
    AZSQL_PASSWORD=<password>
    AZSQL_AUTHENTICATION=<authentication>

    IBM_USERNAME=<username>
    IBM_PASSWORD=<password>
    IBM_HOST=<host>
    IBM_DATABASE=<name>
    IBM_PORT=<port>

    ID_PROJECT==<id_project>
    GOOGLE_APPLICATION_CREDENTIALS=credentials.json

    DRIVER_SQL = <sql_driver>

Then, you need to download *GCP credentials*. For this task, we recommender that you use this `manual <https://cloud.google.com/docs/authentication/getting-started>`_.
The name of  *GCP credentials* should be named *credentials.json*. This file should be on root of the project.

Installation
------------

You need to setup a new python env, activate it and install the requirements

1. Install this repository
.. code-block::
   https://github.com/fralfaro/db-connectors

2. Install python 3.8 with pyenv
.. code-block::
   pyenv install 3.8

3. Set python 3.8
.. code-block::
   pyenv local 3.8

4. Install  `Poetry <https://python-poetry.org/docs/>`_. Then, activate poetry environment on terminal
    * Window: ``%USERPROFILE%\.poetry\bin``
    * linux/mac: ``source $HOME/.poetry/bin``

4. Install **Poetry** dependencies
.. code-block::
   poetry install


Usage
-----

1. Activate Virtual Enviroments with : ``source .env`` or ``export $(cat .env | xargs)``


