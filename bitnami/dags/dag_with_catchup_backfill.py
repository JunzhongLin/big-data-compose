from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'johnlin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_catchup_backfill_v03',
    schedule_interval='@daily',
    start_date=datetime(2022, 7, 1, 12),
    catchup=True,
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is my first task"
    )
    
    task1 