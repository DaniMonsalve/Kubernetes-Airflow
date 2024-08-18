from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Este código define un DAG (Grafico Acíclico Dirigido) en Airflow que realiza dos tareas secuenciales usando el operador BashOperator.

# default_args:
'''
    Especifica los argumentos por defecto para las tareas en el DAG.
    owner: Define quién es el responsable de las tareas.
    start_date: Define la fecha en la que el DAG comenzará a ejecutarse, que es el 15 de agosto de 2024.
    catchup=False: Evita que el DAG ejecute tareas para fechas anteriores a start_date que no se ejecutaron anteriormente.
'''
default_args = {
    'owner': 'daniel983c@gmail.com',
    'start_date': datetime(2024, 8, 15),
    'catchup': False
}

# Definición del DAG: Estructura el flujo de trabajo.
dag = DAG(
    'Pruebas',
    default_args=default_args,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id='hello_world',
    bash_command='echo "Primera tarea ejecutada con exito!!"',
    dag=dag
)

t2 = BashOperator(
    task_id='hello_dml',
    bash_command='echo "Segunda tarea ejecutada con exito!!"',
    dag=dag
)

t1 >> t2  # Define que la tarea t2 (la segunda) debe ejecutarse después de la tarea t1 (la primera).
