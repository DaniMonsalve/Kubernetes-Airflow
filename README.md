# Configuración Personal de Kubernetes y Apache Airflow

Este repositorio con los archivos necesarios para configurar un entorno sencillo de ingeniería de datos usando Kubernetes y Apache Airflow. Este proyecto se ha basado en la estructura del repositorio [Kubernetes for Data Engineering]([https://github.com/ejemplo/repo-original](https://github.com/OmarAlSaghier/Kubernetes-For-DataEngineering)) para configurar el entorno, pero con ajustes y personalizaciones propias.

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

                  .
                  ├── dags
                  │ ├── Extractor.py
                  │ └── Pruebas.py
                  └── k8s
                  │ ├── dashboard-adminuser.yaml
                  │ ├── dashboard-clusterrole.yaml
                  │ ├── dashboard-secret.yaml
                  │ ├── recommended-dashboard.yaml
                  └── values.yaml


### DAGs

- **Extractor.py**: Este DAG utiliza la API de [RandomUser](https://randomuser.me/api/) para obtener datos de prueba. Estos datos se procesan y se utilizan para demostrar el proceso de carga de datos en el entorno de Airflow. La tarea en este script extrae y formatea los datos recibidos de la API, demostrando cómo integrar datos externos en el flujo de trabajo de Airflow.

- **Pruebas.py**: Realiza tareas secuenciales sencillas para demostrar los conceptos básicos de Airflow y la ejecución de tareas en un flujo de trabajo. Este DAG es un ejemplo simple para validar que la configuración del entorno y la ejecución de tareas funcionan correctamente.

### Configuración de Kubernetes (k8s)

- **dashboard-adminuser.yaml**: Archivo YAML para configurar un usuario administrador para el Kubernetes Dashboard.
- **dashboard-clusterrole.yaml**: Archivo YAML que define el rol de clúster para el Kubernetes Dashboard.
- **dashboard-secret.yaml**: Archivo YAML para gestionar los secretos utilizados por el Kubernetes Dashboard.
- **recommended-dashboard.yaml**: Archivo YAML para desplegar la configuración recomendada del Kubernetes Dashboard.
- **values.yaml**: Archivo YAML que contiene valores para personalizar la configuración de Kubernetes.

## Primeros Pasos

### Requisitos Previos

- Un clúster de Kubernetes
- `kubectl` instalado y configurado
- Helm (opcional, pero recomendado para gestionar aplicaciones de Kubernetes)

### Configuración

1. **Desplegar el Kubernetes Dashboard:**

   Para desplegar el Kubernetes Dashboard, aplicar los archivos YAML en el directorio `k8s`:

      ```bash
      kubectl apply -f k8s/

   Esto configurará el Kubernetes Dashboard con los roles y permisos necesarios.

2. **Acceder al Kubernetes Dashboard:**

   Para acceder al Dashboard, iniciar un servidor proxy:

      kubectl proxy

   Luego, accede al Dashboard en: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.

   Utiliza el token generado para el usuario administrador para iniciar sesión (ver dashboard-secret.yaml).

3. **Desplegar Apache Airflow**

   Desplegar Apache Airflow utilizando Helm o aplicando archivos YAML personalizados. Para Helm:

      ```bash
      helm repo add apache-airflow https://airflow.apache.org
      helm install airflow apache-airflow/airflow -f k8s/values.yaml

   Esto desplegará Airflow con la configuración definida en values.yaml.

4. **Añadir DAGs a Airflow**
   Copia los archivos DAG (por ejemplo, Extractor.py, Pruebas.py) en la carpeta DAGs de tu despliegue de Airflow. El método de copia depende de tu configuración de Airflow (por ejemplo, utilizando Persistent Volume, Git-sync).

5. **Tecnologías Utilizadas**
   Kubernetes: Plataforma para automatizar la implementación, escalado y gestión de aplicaciones en contenedores.
   Apache Airflow: Herramienta para la creación, programación y monitorización de flujos de trabajo.
   Python: Lenguaje de programación utilizado para escribir los DAGs de Airflow.
   API de RandomUser: Proporciona datos de prueba para el DAG Extractor.py.

6. **Resultados**
<img width="955" alt="2024-08-17 11_11_50-localhost_8001_1" src="https://github.com/user-attachments/assets/2b2ff74e-ea8c-438b-87d1-edcf54e2d606">
<img width="960" alt="2024-08-17 11_16_53_2" src="https://github.com/user-attachments/assets/5b82e476-7c21-4d9f-9d49-7b3c850917b6">
<img width="953" alt="2024-08-17 11_27_25_3" src="https://github.com/user-attachments/assets/c6905718-2275-488d-9a68-715eaecf6cd1">
<img width="958" alt="2024-08-17 12_09_20_4" src="https://github.com/user-attachments/assets/8d259fe3-1f83-47e0-83ea-cbaf5cb7a485">
<img width="943" alt="2024-08-17 14_16_52-Kubernetes-Airflow_5" src="https://github.com/user-attachments/assets/a5c8f08c-3525-4ab6-9a88-b5feb1c02f7c">
<img width="947" alt="2024-08-17 17_16_59_6" src="https://github.com/user-attachments/assets/54dd5645-d616-47c8-9f6f-d4a4f6ca85f1">
<img width="945" alt="2024-08-17 17_18_14-hello_world - Grid - Airflow_7" src="https://github.com/user-attachments/assets/6b916ceb-a7c4-4bb3-9d25-2ade0147a7d3">
<img width="944" alt="2024-08-17 17_19_36_8" src="https://github.com/user-attachments/assets/28bd299d-be85-475e-8bc2-d668d448fddc">
