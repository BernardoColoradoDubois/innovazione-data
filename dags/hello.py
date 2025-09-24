from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator


def hello_task(**kwargs):
  print("Hello, Airflow!")

dag = DAG(dag_id="hello", start_date=datetime(2022, 1, 1), schedule="0 0 * * *")

hello = PythonOperator(task_id="hello", python_callable=hello_task, dag=dag)

bash_task_1 = BashOperator(task_id="bash_task_1", bash_command="echo 'Hello from Bash 1!'", dag=dag)
bash_task_2 = BashOperator(task_id="bash_task_2", bash_command="echo 'Hello from Bash 2!'", dag=dag)

end = EmptyOperator(task_id="end", dag=dag)

hello >> [bash_task_1, bash_task_2] >> end