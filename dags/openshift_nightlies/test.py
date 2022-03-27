import json
import pathlib
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(dag_id="download_rocket_launches",start_date=airflow.utils.dates.days_ago(14),schedule_interval=None,)

download_launches = BashOperator(task_id="download_launches",bash_command="curl -o /tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",dag=dag,)
get_pictures = BashOperator(task_id="get_pictures",bash_command="curl -o /tmp/launches1.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",dag=dag,)

notify = BashOperator(task_id="notify",bash_command="curl -o /tmp/launches2.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",dag=dag,)

download_launches >> get_pictures >> notify
