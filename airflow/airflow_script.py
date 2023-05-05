#user imports
from utils.utils import _local_to_s3

#airflow imports 
from airflow.models import DAG
#airflow variables at Admin>Variable
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

#Config 
BUCKET_NAME = Variable.get("BUCKET")


#DAG definition
default_args = {'owner': 'airflow','start_date': days_ago(1)}

dag = DAG(
    #how the dag will be named
    dag_id = 'user_behavior', 
    default_args= default_args, 
    schedule_interval=None,
    max_active_runs = 1,
    )

with dag:
    to_raw_data_lake= PythonOperator(
        #dag: (Required)The DAG object to which the task belongs.
        dag=dag,
        #task_id: (Required)A unique identifier for the task.
        task_id="to_raw_data_lake",
        #python_callable: (Required)A Python function will be executed when the task is run.
        python_callable=_local_to_s3,
        #op_kwargs: A dictionary of keyword arguments that will be
        #passed to the python_callable function when the operator calls it.
        op_kwargs={
            #/opt/airflow/ <- basic base file path given in docker-compose.yaml
            #create data folder in plugins
            #/opt/airflow/plugins/data/ 
            # create file name
            #/opt/airflow/data/some_data.csv
            "file_name": "/opt/airflow/plugins/data/some_data.csv",
            # {{ ds }} = is airflow template reference to the
            # DAG run's logical date YYYY-MM-DD
            "key": "raw/some_data/{{ ds }}/some_data.csv",
            "bucket_name": BUCKET_NAME,
        },
    )
    # task2 = BashOperator(
    #     task_id = "run_after_example",
    #     bash_command="mkdir -p data && cd ..; cp /opt/***/file1.csv data"
    # )
    # task3 = PythonOperator(
    #     task_id='run_last',
    #     python_callable= ex_read_func
    # )
 
    to_raw_data_lake
    # task1>>task2
    # task2>>task3