# Email, Slack, MS Teams



# TEAMS ALERT
import json
import requests

def teams_alert(context):
    webhook_url = "https://outlook.office.com/webhook/..."
    message = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "themeColor": "FF0000",
        "title": "Airflow Task Failed",
        "text": f"Task {context['task_instance'].task_id} failed in DAG {context['dag'].dag_id}. [View Log]({context['task_instance'].log_url}"
    }
    headers = {"Content-Type": "application/json"}
    requests.post(webhook_url, headers=headers, data=json.dumps(message))


# EMAIL ALERTS
def send_email_on_failure(context):
    from airflow.utils.email import send_email


    subject = f"Airflow alert: {context['task_instance']}"
    body = f"Task failed. See logs: {context['task_instance'].log_url}"
    send_email(to=["your_email@gmail.com"], subject=subject, html_content=body)

# SLACK ALERT
from airflow.providers.slack.notifications.slack_webhook import SlackWebhookOperator
def slack_alert_legacy(context):
    SlackWebhookOperator(
        task_id='slack_failure',
        http_conn_id='slack_conn_id',
        message=f"Task Failed: {context['task_instance'].task_id}",
        channel='#alerts'
    ).execute(context=context)

    

# SLACK ALERT (old ways of using slack)
def slack_alert(context):
    from airflow.providers.slack.notifications.slack_webhook import send_slack_webhook_notification

    msg = f"""
    :red_circle: Task Failed.
    *DAG*: {context['dag'].dag_id}
    *TASK* {context['task_instance'].task_id}
    *Log URL*: {context['task_instance'].log_url}
    """

    send_slack_webhook_notification(message=msg, webhook_token='YOUR_SLACK_WEBHOOK_TOKEN')
