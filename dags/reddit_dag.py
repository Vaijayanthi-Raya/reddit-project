
from datetime import datetime
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the reddit_pipeline function from reddit_pipeline.py
from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Vaijayanthi Raya',
    'start_date': datetime(2024, 10, 4),  # Set a fixed date in the past
    'retries': 1,
}

dag = DAG(
    dag_id='reddit_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'filename': f'reddit_{datetime.now().strftime("%Y%m%d")}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# Upload to S3 task will go here
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3


