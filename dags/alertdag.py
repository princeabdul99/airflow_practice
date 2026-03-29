from airflow.sdk import Asset, dag, task
from pendulum import datetime
from airflow.utils.dates import days_ago # deprexcating soon

from include import send_email_on_failure

import requests


# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=days_ago(1),
    schedule="@none",
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["Alert"],
)
def email_alert_dag():
    @task(on_failure_callback=lambda context: send_email_on_failure(context))
    def fail_task():
        raise ValueError("Triggering failure")
    
    fail_task()

email_alert_dag()    