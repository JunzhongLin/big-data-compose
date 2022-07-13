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
    dag_id='dag_with_cron_expr_v02',
    schedule_interval='0 5 * * 2,3,4',
    start_date=datetime(2022, 6, 20),
    catchup=True,
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is my first task"
    )
    
    task1 