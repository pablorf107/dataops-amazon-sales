# DataOps Amazon Sales Pipeline

## 1. Descripción del proyecto

Este proyecto consiste en el diseño e implementación de un pipeline DataOps para automatizar el tratamiento y análisis de datos de ventas de Amazon.

El objetivo principal es construir un flujo reproducible que permita extraer datos desde un archivo CSV, validarlos, limpiarlos, transformarlos y generar datasets procesados que posteriormente son utilizados por un dashboard interactivo desarrollado con Streamlit.

El proyecto incluye:

- Pipeline ETL desarrollado en Python.
- Validación y limpieza de datos.
- Generación automática de datasets procesados.
- Dashboard analítico interactivo.
- Tests automáticos con cobertura superior al 70%.
- Workflow de integración continua con GitHub Actions.
- Dockerfile para ejecución reproducible.
- Código de infraestructura como código mediante Terraform.

---

## 2. Arquitectura del proyecto

El flujo general del proyecto es el siguiente:

```text
CSV original
    ↓
Extracción de datos
    ↓
Validación de columnas y estructura
    ↓
Limpieza y transformación
    ↓
Generación de datasets procesados
    ↓
Dashboard interactivo
    ↓
Tests + CI/CD + Docker + Terraform