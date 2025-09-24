from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

dag = DAG(dag_id="hello", start_date=datetime(2022, 1, 1), schedule="0 0 * * *")


list_packages = BashOperator(task_id="list_packages", bash_command="pip list", dag=dag)