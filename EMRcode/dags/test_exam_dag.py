#imports
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime

#python function for creating csv from dataframe from lists
def create_new_csv(ti):
        age=[36,55,61,65,53,50,28,62,48,31,57,44,38]
        gender=['F','F','M','F','F','F','F','F','M','M','F','M','M']
        education=['College','College','Grad','College','Grad','Grad','College','College','Grad','Grad','College','College','College']
        maritalStatus=['D','D','W','M','M','M','M','D','M','M','M','M','M']
        df = pd.DataFrame(
        {'Age': age,
         'Gender': gender,
         'Education': education,
         'MaritalStatus': maritalStatus   
        }
        )
        return df.to_csv('generalInfo.csv')

#function to pull CSV from first task
def pull_CSV(ti):
    pulled = ti.xcom_pull(task_ids["first_task"])
    #if not pulled:
    #    raise new Exception("Unable to successfully pull CSV file.")

#function to retrieve/print new csv
def retrieve_csv(ti):
    result = pd.read_csv(Variable.get('exam_csv_path'))
        #exam_csv_path: /Users/matts/Desktop/generalInfo.csv, stored locally and on Airflow webserver UI
    print(result)
        
#alternate solution without bash
def print_CSV(ti):
    pulled = ti.xcom_pull(task_ids["first_task"])
    result = pd.read_csv(pulled)
    print(result)

with DAG(
    dag_id="test_exam_dag", # Dag ID 
    schedule_interval='* * * * *',  # per min
    catchup=False  # Catchup not needed 
) as dag:
    
    #create DataFrame using lists provided and save to CSV file
    task1 = PythonOperator(
        task_id="first_task"
        python_callable=create_new_csv
        #do_xcom_push=True
    )

    task3
    
    #copy into directory using bashOp
    task2 = BashOperator(
        task_id="second_task"
        bash_command="cp $FILE $PATH" #cp should create new dir if path not found?
        env={"FILE": pull_CSV, "PATH": Variable.get('exam_csv_path')}
        #exam_csv_path: /Users/matts/Desktop/generalInfo.csv, stored locally and on Airflow webserver UI
    )
    
    #workaround solution since stumped on bashop
    #task2 = PythonOperator(
    #    task_id="alternate_task"
    #    python_callable=print_CSV
    #) 
    
     #read created file from dir, print out contents to log
    task3 = PythonOperator(
        task_id="third_task"
        python_callable=retrieve_csv
    )
    
    #hierarchy
    #task1 >> task2 #>> task3