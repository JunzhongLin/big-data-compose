from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args: dict = {
    'owner': 'johnlin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='dag_with_taskflow_api_v4',
    default_args=default_args,
    start_date=datetime(2022, 7, 4, 22),
    schedule_interval='@daily'
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'fname': 'John',
            'lname': 'Lin'
        }

    @task()
    def get_age():
        return 20

    @task()
    def greet(fname, lname, age):
        print(f'hello world, this is {fname} {lname},'
              f' I am {age} years old')

    name_dict = get_name()
    age = get_age()
    greet(
        fname=name_dict['fname'],
        lname=name_dict['lname'],
        age=age
    )


greet_dag = hello_world_etl()
