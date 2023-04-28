

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
default_args = {
 
    'owner': 'airflow',
    'start_date': days_ago(1)
}



dag = DAG(
    #how the dag will be named
    dag_id = 'user_behavior', 
    default_args= default_args, 
    schedule_interval=None,
    max_active_runs = 1,
    )


######functions ####################################################################








review_to_raw_data_lake = PythonOperator(
    dag=dag,
    task_id="movie_review_to_raw_data_lake",
    python_callable=_local_to_s3,
    op_kwargs={
        "file_name": "/opt/airflow/data/movie_review.csv",
        "key": "raw/movie_review/{{ ds }}/movie.csv",
        "bucket_name": BUCKET_NAME,
    },
)
##################################################################################
with dag:
    task1= PythonOperator(
        task_id='run_this_example',
        python_callable = review_to_raw_data_lake
    )
    # task2 = BashOperator(
    #     task_id = "run_after_example",
    #     bash_command="mkdir -p data && cd ..; cp /opt/***/file1.csv data"
    # )
    # task3 = PythonOperator(
    #     task_id='run_last',
    #     python_callable= ex_read_func
    # )
 
    task1
    # task1>>task2
    # task2>>task3
