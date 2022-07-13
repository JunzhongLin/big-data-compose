# big-data-compose
----

## What is this repo about?
----

This repo is mean to provide a playground for the big-data applications, such as Spark, Hive, Hadoop, Airflow, etc. I would like to make the environment setup and tear-down as easy as possible. Currently, Spark, Livy, Airflow have been added in the docker-compose.yml. In this repo, I provided a simple wordcount job as a demo. More demos will be added in the future.

For the airflow setup, I simplified the environment from bitnami's official compose by using a LocalExecutor: https://github.com/bitnami/bitnami-docker-airflow

## Prerequisites
----
To run this application you need Docker Engine >= 1.10.0. Docker Compose is recommended with a version 1.6.0 or later.

## Application version in use
| Application | Version | Comment |
|:---:|:---:|:---:|
|Python|3.7.11| |
|Spark|2.3.2| |
|Hadoop|2.7| |
|Livy|0.7.0| |
|Airflow|2.2.3| |
|Postgres|10||


## Folder structure
----
```bash
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── bitnami
│   ├── dags
│   │   ├── dag_livy_test.py
│   │   ├── dag_with_catchup_backfill.py
│   │   ├── dag_with_cron_expr.py
│   │   ├── dag_with_pgres.py
│   │   └── dag_with_taskflow_api.py
│   ├── docker-compose.yml
│   └── requirements.txt
├── docker_files
│   ├── livy-spark
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── log4j.properties
│   ├── spark_base
│   │   └── Dockerfile
│   └── spark_dep
│       ├── Dockerfile
│       └── start-spark.sh
└── test_case
    ├── app
    │   ├── dependencies
    │   │   ├── __init__.py
    │   │   ├── logging_.py
    │   │   └── spark.py
    │   ├── livy_submit
    │   └── wordcount.py
    ├── build_packages.sh
    ├── data
    │   └── countme.txt
    ├── packages.zip
    └── readme.MD
```

## How to use this repo:
----

### Build up the base docker-images:
----

- build up the spark-base image:
    enter the folder 'spark_base' under 'docker_files' and run:
    ```bash
    docker build --tag john/pyspark:2.3.2-hadoop2.7-py3.7 .
    ```
- build up the livy-spark image:
    enter the folder 'livy-spark' under 'docker_files' and run:
    ```bash
    docker build --tag --tag john/livy-spark:0.3.0 .
    ```
- build up the pyspark image (python dependencies can be added in this step):
    enter the folder 'spark_dep' under 'docker_files' and run:
    ```bash
    docker build --tag standalone-pyspark:2.3.2-hadoop2.7-py3.7 .
    ```

- compose up
    enter the root folder of this project
    ```bash
    docker compose up
    ```



