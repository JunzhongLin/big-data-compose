from nis import cat
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.apache.livy.operators.livy import LivyOperator

default_args = {
    'owner': 'johnlin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# pyspark_code = """
# import sys
# print(sys.version)
# spark.range(1000 * 1000 * {{params.your_number}}).count()
# df = sqlContext.createDataFrame(
#     [("This was Python code", 0), ("One", 1), ("Two", 2), ("Three", 3), ("Four", 4)],
#     ("{{ params.your_string }}", "{{ run_id }}"),
# )
# df.show()
# """

with DAG(
    dag_id='dag_with_livy_v02',
    default_args=default_args,
    start_date=datetime(2022, 7, 11),
    schedule_interval=None,
    catchup=False
) as dag:

    task1 = LivyOperator(
        task_id='wordcount_test',
        file='/job/app/wordcount.py',
        py_files=[
            '/job/app/wordcount.py',
            '/job/packages.zip'
        ],
        files=['/job/data/countme.txt']
    )

    task1