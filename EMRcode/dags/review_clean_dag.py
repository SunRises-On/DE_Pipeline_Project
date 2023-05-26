import json
from datetime import datetime, timedelta

from utils.utils import _local_to_s3, run_redshift_external_query

from airflow import DAG
from airflow.contrib.operators.emr_add_steps_operator import (
    EmrAddStepsOperator,
)
from airflow.contrib.sensors.emr_step_sensor import EmrStepSensor
from airflow.models import Variable

# Configs
BUCKET_NAME = Variable.get("BUCKET")
EMR_ID = Variable.get("EMR_ID")
##TO DO##:EMR_STEPS = {}
#with open("./dags/scripts/emr/clean_restaurant_review.json") as json_file:
#    EMR_STEPS = json.load(json_file)

dag = DAG(
    #how the dag will be named
    dag_id = 'user_behavior', 
    default_args= default_args, 
    schedule_interval=None,
    max_active_runs = 1,
    )



review_to_raw_data_lake = PythonOperator(
    dag=dag,
    task_id="review_to_raw_data_lake",
    python_callable=_local_to_s3,
    op_kwargs={
        "file_name": "/opt/airflow/data/order_review.csv",
        "key": "raw/order_review/{{ ds }}/restaurant.csv",
        "bucket_name": BUCKET_NAME,
    },
)

spark_script_to_s3 = PythonOperator(
    dag=dag,
    task_id="spark_script_to_s3",
    python_callable=_local_to_s3,
    op_kwargs={
        "file_name": "./dags/scripts/random_text_classification.py",
        "key": "scripts/random_text_classification.py",
        "bucket_name": BUCKET_NAME,
    },
)

#NEED FIX
start_emr_classification_script = EmrAddStepsOperator(
    dag=dag,
    task_id="start_emr_classification_script",
    job_flow_id=EMR_ID,
    aws_conn_id="aws_default",
    #steps=EMR_STEPS,
    params={
        "BUCKET_NAME": BUCKET_NAME,
        "raw_order_review": "raw/order_review",
        "text_classifier_script": "scripts/random_text_classifier.py",
        "stage_order_review": "stage/order_review",
    },
    depends_on_past=True,
)
#FIX
#last_step = len(EMR_STEPS) - 1

wait_for_classification_transformation = EmrStepSensor(
    dag=dag,
    task_id="wait_for_classification_transformation",
    job_flow_id=EMR_ID,
    step_id='{{ task_instance.xcom_pull\
        ("start_emr_classification_script", key="return_value")['
    + str(last_step)
    + "] }}",
    depends_on_past=True,
)


#path stuff
(
    [
        review_to_raw_data_lake,
        spark_script_to_s3,
    ]
    >> start_emr_classification_script
    >> wait_for_classification_transformation
)