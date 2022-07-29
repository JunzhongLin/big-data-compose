# big-data-compose
----

## What is this repo about?
----

This repo is mean to provide a playground for the big-data applications, such as Spark, Hive, Hadoop, Airflow, etc. I would like to make the environment setup and tear-down as easy as possible. In this repo different docker compose setups have been added into specific sub-folders, such as standalone spark, spark on yarn etc. An wordcounting example is provided for testing purpose.

For the airflow setup, The environment from bitnami's official compose setup is simplified by using a LocalExecutor: https://github.com/bitnami/bitnami-docker-airflow

## Prerequisites
----
To run this application you need Docker Engine >= 1.10.0. Docker Compose is recommended with a version 1.6.0 or later.

## Application version in use
| Application | Version | Comment |
|:---:|:---:|:---:|
|Python|3.7.11| |
|Spark|2.3.2/2.4.1| |
|Hadoop|2.7| |
|Livy|0.7.0| |
|Airflow|2.2.3| |
|Hive|3.1.2| |
|Postgres|10/11.5| |


## Folder structure
----
```bash
.
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── bitnami
│   ├── dags
│   └── requirements.txt
├── standalone-spark-livy-airflow
│   ├── README.md
│   ├── dags
│   │   ├── dag_livy_test.py
│   │   ├── dag_with_catchup_backfill.py
│   │   ├── dag_with_cron_expr.py
│   │   ├── dag_with_pgres.py
│   │   └── dag_with_taskflow_api.py
│   ├── docker-compose.yml
│   ├── docker_files
│   │   ├── livy-spark
│   │   │   ├── Dockerfile
│   │   │   ├── entrypoint.sh
│   │   │   └── log4j.properties
│   │   ├── spark_base
│   │   │   └── Dockerfile
│   │   └── spark_dep
│   │       ├── Dockerfile
│   │       └── start-spark.sh
│   ├── requirements.txt
│   └── test_case
│       ├── app
│       │   ├── dependencies
│       │   │   ├── __init__.py
│       │   │   ├── logging_.py
│       │   │   └── spark.py
│       │   ├── livy_submit
│       │   └── wordcount.py
│       ├── build_packages.sh
│       ├── data
│       │   └── countme.txt
│       ├── packages.zip
│       └── readme.MD
├── test_case
│   └── app
│       └── dependencies
├── yarn-spark
│   ├── README.md
│   ├── docker-compose.yml
│   ├── dockerfiles
│   │   └── yarn-spark-base
│   │       ├── Dockerfile
│   │       ├── config
│   │       │   ├── core-site.xml
│   │       │   ├── hadoop-env.sh
│   │       │   ├── hdfs-site.xml
│   │       │   ├── mapred-site.xml
│   │       │   ├── slaves
│   │       │   ├── spark
│   │       │   │   ├── log4j.properties
│   │       │   │   ├── spark-env.sh
│   │       │   │   └── spark.defaults.conf
│   │       │   ├── ssh_config
│   │       │   └── yarn-site.xml
│   │       └── scripts
│   │           ├── entrypoint.sh
│   │           ├── spark-services.sh
│   │           └── wait-for-it.sh
│   └── test_case
│       ├── app
│       │   ├── dependencies
│       │   │   ├── __init__.py
│       │   │   ├── logging_.py
│       │   │   └── spark.py
│       │   ├── livy_submit
│       │   └── wordcount.py
│       ├── build_packages.sh
│       ├── data
│       │   └── countme.txt
│       ├── packages.zip
│       └── readme.MD
├── yarn-spark-hive
│   ├── README.md
│   ├── docker-compose.yml
│   ├── dockerfiles
│   │   └── base
│   │       ├── Dockerfile
│   │       ├── config
│   │       │   ├── core-site.xml
│   │       │   ├── hadoop-env.sh
│   │       │   ├── hdfs-site.xml
│   │       │   ├── hive
│   │       │   │   └── hive-site.xml
│   │       │   ├── mapred-site.xml
│   │       │   ├── slaves
│   │       │   ├── spark
│   │       │   │   ├── log4j.properties
│   │       │   │   ├── spark-env.sh
│   │       │   │   └── spark.defaults.conf
│   │       │   ├── ssh_config
│   │       │   └── yarn-site.xml
│   │       └── scripts
│   │           ├── entrypoint.sh
│   │           ├── spark-services.sh
│   │           └── wait-for-it.sh
│   └── init.sql
└── yarn-spark-livy
    ├── README.md
    ├── docker-compose.yml
    ├── dockerfiles
    │   └── spark-livy
    │       ├── Dockerfile
    │       ├── config
    │       │   ├── core-site.xml
    │       │   ├── hadoop-env.sh
    │       │   ├── hdfs-site.xml
    │       │   ├── livy
    │       │   │   └── livy-env.sh
    │       │   ├── mapred-site.xml
    │       │   ├── slaves
    │       │   ├── spark
    │       │   │   ├── log4j.properties
    │       │   │   ├── spark-env.sh
    │       │   │   └── spark.defaults.conf
    │       │   ├── ssh_config
    │       │   └── yarn-site.xml
    │       ├── entrypoint.sh
    │       └── log4j.properties
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
Please enter the specific sub-folder and refer to the README.md file inside

typically, individual docker image should be built up from the docker files provided. Then the environment can be composed up using yaml file in the subfolder



