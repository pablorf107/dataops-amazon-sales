# DataOps Amazon Sales Pipeline

## Descripción del proyecto

Este proyecto consiste en el diseño e implementación de un pipeline DataOps para automatizar el tratamiento y análisis de datos de ventas de Amazon India. El objetivo principal es construir un flujo reproducible que permita partir de un archivo CSV original, validar su estructura, limpiar y transformar los datos, generar datasets procesados y visualizarlos posteriormente mediante un dashboard interactivo desarrollado con Streamlit.

El proyecto se ha planteado como una solución sencilla pero completa, incorporando las principales fases de un flujo DataOps: extracción, validación, transformación, carga, visualización, tests, integración continua, contenedorización, infraestructura como código y metodología ágil.

## Arquitectura del proyecto

El flujo general del proyecto es el siguiente:

CSV original → Extracción de datos → Validación de estructura → Limpieza y transformación → Generación de datasets procesados → Dashboard interactivo → Tests + CI/CD + Docker + Terraform

La estructura principal del repositorio es:

dataops-amazon-sales/
- data/
  - raw/
    - Amazon Sale Report.csv
  - processed/
- src/
  - extract.py
  - validate.py
  - transform.py
  - load.py
  - pipeline.py
- dashboard/
  - app.py
- tests/
  - test_extract.py
  - test_load.py
  - test_transform.py
  - test_validate.py
- infra/
  - main.tf
  - variables.tf
  - outputs.tf
- .github/workflows/
  - ci.yml
- Dockerfile
- requirements.txt
- pytest.ini
- README.md

## Dataset utilizado

El dataset utilizado es `Amazon Sale Report.csv`, que contiene información sobre pedidos, ventas y logística de Amazon India. Entre sus variables principales se encuentran `Order ID`, `Date`, `Status`, `Fulfilment`, `Category`, `Qty`, `Amount`, `ship-city`, `ship-state`, `ship-country` y `B2B`.

Estas variables permiten realizar análisis comerciales y logísticos, como ventas totales, número de pedidos, unidades vendidas, ticket medio, evolución temporal, ventas por categoría, pedidos por estado, ventas por región y comparación entre clientes B2B y B2C.

El dataset original se almacena en `data/raw/`, mientras que los archivos generados por el pipeline se guardan en `data/processed/`.

## Proceso ETL

El pipeline está dividido en cuatro fases principales:

1. Extracción: el archivo `src/extract.py` carga el dataset original desde la carpeta `data/raw/`.

2. Validación: el archivo `src/validate.py` comprueba que el dataset no esté vacío y que contenga las columnas obligatorias necesarias para el análisis.

3. Transformación: el archivo `src/transform.py` realiza la limpieza y preparación de los datos. Entre las operaciones realizadas se incluyen la eliminación de columnas innecesarias, la normalización de nombres de columnas, la conversión de fechas, la conversión de variables numéricas, el tratamiento de valores nulos y la creación de nuevas variables analíticas como `year`, `month`, `month_name`, `order_status_group` y `customer_type`.

4. Carga: el archivo `src/load.py` guarda el dataset limpio y varios archivos agregados en la carpeta `data/processed/`.

Los archivos generados por el pipeline son:

- amazon_sales_clean.csv
- sales_by_month.csv
- sales_by_category.csv
- sales_by_state.csv
- sales_by_status.csv

El pipeline completo se ejecuta desde `src/pipeline.py`.


## Dashboard

El dashboard se ha desarrollado con Streamlit y Plotly. Su objetivo es facilitar la exploración visual e interactiva de los datos procesados por el pipeline.

Incluye indicadores principales como ventas totales, número de pedidos, unidades vendidas, ticket medio y tasa de cancelaciones. También incorpora gráficos de evolución temporal, ventas por categoría, distribución de pedidos por estado, top regiones por ventas, comparación entre clientes B2B y B2C y análisis por tipo de fulfilment.

Además, el dashboard permite filtrar los datos por rango de fechas, categoría, estado del pedido, región, tipo de cliente y tipo de fulfilment. También incluye una tabla con los datos filtrados y la posibilidad de descargarlos en formato CSV.

## Tests y cobertura

El proyecto utiliza `pytest` y `pytest-cov` para comprobar el correcto funcionamiento del pipeline. Los tests se encuentran en la carpeta `tests/` y cubren las principales fases del proceso: extracción, validación, transformación y carga.

Para ejecutar los tests:

pytest

Para ejecutar los tests con cobertura:

pytest --cov=src --cov-report=term-missing

El resultado obtenido fue de 13 tests superados y una cobertura total del 76%, superando el mínimo del 70% establecido para el proyecto.

## Integración continua con GitHub Actions

El proyecto incluye un workflow de GitHub Actions ubicado en `.github/workflows/ci.yml`. Este workflow se ejecuta automáticamente en cada `push` o `pull request` sobre las ramas `main` o `master`.

El proceso de integración continua realiza la descarga del repositorio, configura Python 3.11, instala las dependencias, ejecuta los tests y comprueba que la cobertura mínima sea del 70%. De esta forma, cualquier cambio subido al repositorio queda validado automáticamente.

## Docker

El proyecto incluye un `Dockerfile` para facilitar la ejecución reproducible de la aplicación. Docker permite empaquetar el proyecto junto con sus dependencias, evitando problemas derivados de configuraciones locales diferentes.

Para construir la imagen:

docker build -t dataops-amazon-sales .

Para ejecutar el contenedor:

docker run -p 8501:8501 dataops-amazon-sales

Después se puede acceder al dashboard desde:

http://localhost:8501

## Infraestructura como código

La carpeta `infra/` contiene una definición básica de infraestructura como código mediante Terraform. La infraestructura propuesta consiste en un bucket S3 de AWS para almacenar datasets procesados o artefactos generados por el pipeline.

Los archivos incluidos son:

- infra/main.tf
- infra/variables.tf
- infra/outputs.tf

Comandos teóricos para desplegar la infraestructura:

cd infra  
terraform init  
terraform plan  
terraform apply

Para eliminar los recursos:

terraform destroy

Aunque el despliegue cloud no es el objetivo principal del proyecto, esta parte permite mostrar cómo la solución podría evolucionar hacia una arquitectura DataOps más completa en AWS.

## Metodología ágil

El proyecto se ha organizado siguiendo una metodología ágil sencilla basada en SCRUM/Kanban. Se ha definido un Product Backlog con User Stories, tres sprints de trabajo y una retrospectiva final.

Los sprints planteados han sido:

- Sprint 1: preparación del dataset y construcción del pipeline ETL.
- Sprint 2: desarrollo del dashboard y creación de tests.
- Sprint 3: incorporación de Docker, GitHub Actions, Terraform y documentación.

Además, se ha creado un tablero Kanban en GitHub Projects con columnas como `Product Backlog`, `To Do`, `In Progress`, `Review` y `Done`.

## Decisiones técnicas

Las principales herramientas utilizadas han sido Python, pandas, Streamlit, Plotly, pytest, pytest-cov, GitHub Actions, Docker, Terraform y GitHub Projects.

Python se ha utilizado como lenguaje principal por su utilidad en proyectos de ciencia de datos. pandas se ha empleado para la limpieza y transformación de datos. Streamlit y Plotly se han usado para desarrollar el dashboard interactivo. pytest y pytest-cov han permitido validar el código y medir la cobertura. GitHub Actions se ha usado para automatizar los tests. Docker se ha incluido para mejorar la reproducibilidad. Terraform se ha utilizado para introducir infraestructura como código y GitHub Projects para organizar el trabajo mediante metodología ágil.

## Conclusiones

El proyecto demuestra cómo aplicar un enfoque DataOps a un caso práctico de análisis de ventas. A partir de un archivo CSV original, se ha construido un pipeline capaz de extraer, validar, limpiar, transformar y cargar datos procesados de forma automática.

Estos datos alimentan un dashboard interactivo que permite analizar indicadores comerciales y logísticos de manera sencilla. Además, el proyecto incorpora buenas prácticas de desarrollo y despliegue, como tests automáticos, medición de cobertura, integración continua con GitHub Actions, Docker, Terraform, documentación y metodología ágil.

Como mejoras futuras, se podría incorporar un orquestador como Prefect o Airflow, conectar el pipeline directamente con AWS S3, desplegar el dashboard en la nube o añadir análisis más avanzados, como predicción de ventas o alertas sobre cancelaciones.