# Configuración Personal de Kubernetes y Apache Airflow

Este repositorio contiene una configuración personalizada para un entorno de ingeniería de datos utilizando Kubernetes y Apache Airflow. Este proyecto se ha basado en la estructura del repositorio [Kubernetes for Data Engineering](https://github.com/ejemplo/repo-original) para configurar el entorno, pero con ajustes y personalizaciones propias.

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

                  .
                  ├── dags
                  │ ├── Extractor.py
                  │ └── Pruebas.py
                  └── k8s
                  ├── dashboard-adminuser.yaml
                  ├── dashboard-clusterrole.yaml
                  ├── dashboard-secret.yaml
                  ├── recommended-dashboard.yaml
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

   Para desplegar el Kubernetes Dashboard, aplica los archivos YAML en el directorio `k8s`:

      ```bash
      kubectl apply -f k8s/

   Esto configurará el Kubernetes Dashboard con los roles y permisos necesarios.

2. **Acceder al Kubernetes Dashboard:**

   Para acceder al Dashboard, puede que necesites iniciar un servidor proxy:

      kubectl proxy

   Luego, accede al Dashboard en: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.

   Utiliza el token generado para el usuario administrador para iniciar sesión (ver dashboard-secret.yaml).

3. **Desplegar Apache Airflow**

   Puedes desplegar Apache Airflow utilizando Helm o aplicando archivos YAML personalizados. Para Helm:

      ```bash
      helm repo add apache-airflow https://airflow.apache.org
      helm install airflow apache-airflow/airflow -f k8s/values.yaml

   Esto desplegará Airflow con la configuración definida en values.yaml.

4. **Añadir DAGs a Airflow**
   Copia tus archivos DAG (por ejemplo, Extractor.py, Pruebas.py) en la carpeta DAGs de tu despliegue de Airflow. El método de copia depende de tu configuración de Airflow (por ejemplo, utilizando Persistent Volume, Git-sync).

5. **Tecnologías Utilizadas**
   Kubernetes: Plataforma para automatizar la implementación, escalado y gestión de aplicaciones en contenedores.
   Apache Airflow: Herramienta para la creación, programación y monitorización de flujos de trabajo.
   Python: Lenguaje de programación utilizado para escribir los DAGs de Airflow.
   API de RandomUser: Proporciona datos de prueba para el DAG Extractor.py.

6. **Resultados**