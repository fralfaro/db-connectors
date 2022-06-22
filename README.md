# Common Connectors

[![YourActionName Actions Status](https://github.com/fralfaro/db-connectors/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/fralfaro/db-connectors/actions)
<a href="https://fralfaro.github.io/db-connectors/"><img alt="Link a la Documentación" src="https://img.shields.io/badge/docs-link-brightgreen"></a>
[![codecov](https://codecov.io/gh/fralfaro/db-connectors/branch/master/graph/badge.svg)](https://codecov.io/gh/fralfaro/db-connectors)

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/static--analysis-black%20flake8-black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/testing-pytest-black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/documentation-sphinx-black"></a>

All common connectors.

## About The Project

The main goal is use the same repository to connect data and use same enviroment variables.
The connectors that we have are: **PDW**, **IBM**, **AZSQL** and **BIG QUERY**.

## Getting Started

You need to setup a new env with python 3.8+ and some environment variables.

### Prerequisites

You need a file named `.env` on root of the project, this file look like this:

 ```sh
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
 ```
Then, you need to download *BIG QUERY credentials*. For this task, we recommender that you use this [manual](https://cloud.google.com/docs/authentication/getting-started).
The name of  *BIG QUERY credentials* should be named *bq_credentials.json*. This file should be on root of the project.

### Installation
You need to setup a new python env, activate it and install the requirements
1. Install this repository
   ```sh
   https://github.com/fralfaro/db-connectors
   ```
2. Install python 3.8 with pyenv
   ```sh
   pyenv install 3.8
    ```
3. Set python 3.8
   ```sh
   pyenv local 3.8
   ```
4. Install  [Poetry](https://python-poetry.org/docs/). Then, activate poetry environment on terminal
    * Window: ` %USERPROFILE%\.poetry\bin`
    * linux/mac: `source $HOME/.poetry/bin`

4. Install <b>Poetry</b> dependencies
   ```sh
   poetry install
   ```


## Usage

1. Activate Virtual Enviroments with : `source .env`or `export $(cat .env | xargs) `


