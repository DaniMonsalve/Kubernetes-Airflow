import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Argumentos por defecto para las tareas en el DAG
default_args = {
    'owner': 'daniel983c@gmail.com',
    'start_date': datetime(2024, 8, 15, 17, 0)
}

# Definición del DAG: Estructura el flujo de trabajo
dag = DAG(
    'extractor',  # Nombre del DAG
    default_args=default_args,
    schedule_interval=None  # Definimos que no tenga un schedule, para que se ejecute manualmente
)

# Función para obtener datos de la API
def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    # Imprimir los datos en crudo
    print("Datos crudos obtenidos de la API:")
    print(res)

    return res

# Función para formatear los datos obtenidos
def format_data(res):
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    # Imprimir los datos formateados
    print("Datos formateados:")
    print(data)

    return data

# Definir la primera tarea para obtener los datos
get_data_task = PythonOperator(
    task_id='get_data',  # Nombre de la tarea
    python_callable=get_data,  # Función Python a ejecutar
    dag=dag
)

# Definir la segunda tarea para formatear los datos obtenidos
format_data_task = PythonOperator(
    task_id='format_data',  # Nombre de la tarea
    python_callable=format_data,  # Función Python a ejecutar
    op_args=['{{ ti.xcom_pull(task_ids="get_data") }}'],  # Pasa los datos obtenidos por la primera tarea
    dag=dag
)

# Definir la secuencia de las tareas
get_data_task >> format_data_task  # La tarea 'format_data' depende de 'get_data'
