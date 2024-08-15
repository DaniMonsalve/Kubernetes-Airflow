from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Este código define un DAG (Directed Acyclic Graph) en Airflow que realiza dos tareas secuenciales usando el operador BashOperator. 

#default_args:
'''
    Especifica los argumentos por defecto para las tareas en el DAG.
    owner: Define quién es el propietario de las tareas.
    start_date: Define la fecha de inicio del DAG, que es el 15 de agosto de 2024.
    catchup=False: Evita que el DAG ejecute todas las fechas anteriores desde start_date hasta la fecha actual si no ha sido ejecutado antes.
'''
default_args = {
    'owner': 'daniel983c@gmail.com',
    'start_date': datetime(2024, 8, 15),
    'catchup': False
}

# DAG de airflow: Define la estructura del flujo de trabajo.
dag = DAG(
    'hello_world',
    default_args = default_args,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_dml',
    bash_command='echo "Hello Data Mastery Lab"',
    dag = dag
)

t1 >> t2 #Define que t2 (la segunda tarea) debe ejecutarse después de t1 (la primera tarea).