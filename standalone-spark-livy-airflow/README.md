

## How to use this repo:

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