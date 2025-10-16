# Diseño e Implementación de un Pipeline ETL para la Integración y Análisis de Ventas E-Commerce (2023-2025)

**Autor:** Ing. Rubén Soria\
**Docente:** Ing. Anthony Huaccachi\
**Especialización:** Ingeniería de Datos e Inteligencia Artificial con
Databricks

------------------------------------------------------------------------

## Descripción General

Este proyecto tiene como objetivo **implementar un proceso ETL
completo** (Extract, Transform, Load) para consolidar y disponibilizar
la información de ventas generadas por el canal **e-commerce** entre los
años **2023 y 2025**.
El desarrollo se realizó en **Microsoft Azure**, utilizando
**Databricks** como plataforma principal para la ingeniería de datos,
siguiendo el **patrón de arquitectura Medallion** (Bronze, Silver,
Golden).

------------------------------------------------------------------------

## Objetivo del Proyecto

Desarrollar un proceso automatizado que permita:

-   Extraer datos de diversas fuentes transaccionales del e-commerce.
-   Transformar y limpiar los datos para garantizar su integridad y
    consistencia.
-   Cargar los datos normalizados en un **repositorio centralizado**.
-   Disponibilizar la información para su análisis mediante **Power BI**
    y otras herramientas BI.

### Características del ETL

-   Estructura y normalización del modelo de datos.
-   Depuración de duplicados y validaciones de calidad.
-   Actualización periódica (diaria o semanal).
-   Exposición en base de datos **Azure SQL Database**.

------------------------------------------------------------------------

## Arquitectura del Proyecto


<img width="425" height="233" alt="image" src="https://github.com/user-attachments/assets/2d099b1e-615b-4764-a5b2-a630030e6447" />



El proyecto se implementa íntegramente en **Azure Cloud**, aprovechando
sus servicios nativos:

  Servicio               Nombre
  ---------------------- -------------------
  Storage Account        `adlsecommerce`
  Access Connector       `ac-ecommerce`
  Container              `metastore-prod`
  Databricks Workspace   `prod-ecommerce`
  Azure SQL Server       `serverecommerce`
  Azure SQL Database     `ecommerce`

### Patrón Medallion

El flujo de datos sigue las capas: 
1. **Raw / Bronze:** Datos originales
sin procesar.
2. **Silver:** Datos transformados y validados.
3. **Golden:** Datos listos para análisis y consumo BI.

------------------------------------------------------------------------

##  Implementación Técnica


<img width="398" height="231" alt="image" src="https://github.com/user-attachments/assets/4af6bc94-e41f-4829-8ae2-346cd74d2202" />



###  Configuración en Ambiente Develop

-   Creación del **Storage Account** con contenedores: `metastoredata`,
    `raw`, `bronze`, `silver`, `golden`.
-   Carga de la fuente: `Ecommerce_Sales_Prediction_Dataset.csv`.
-   Configuración de **Managed Identity** y **External Location**.
-   Creación de un **Metastore** dedicado para aislar entornos de
    desarrollo y producción.

###  Creación de Notebooks

**Dataset fuente:** `Ecommerce_Sales_Prediction_Dataset.csv`
| Columna | Descripción |
|---------|-------------|
| `Date` | Fecha de la venta (desde 01-01-2023) |
| `Product_Category` | Categoría del producto |
| `Price` | Precio del producto |
| `Discount` | Descuento aplicado |
| `Customer_Segment` | Segmento del comprador |
| `Marketing_Spend` | Presupuesto de marketing |
| `Units_Sold` | Unidades vendidas |

Exploración inicial de datos y validaciones de consistencia.

###  Workflow y Ejecución

Durante la prueba del workflow, se presentó un error en la tarea
`task_transform` debido a la configuración ANSI de Spark.
Se resolvió mediante:

``` python
spark.conf.set("spark.sql.ansi.enabled", "false")
```

Tras la corrección, el **workflow finalizó exitosamente**, generando
catálogos, esquemas y tablas **Delta Parquet**.

------------------------------------------------------------------------

## CI/CD con GitHub Actions

Se configuraron **secretos y workflows de despliegue automatizado**
mediante **GitHub Actions**.
- Archivo `script.yml` contiene la orquestación del pipeline.
- Cada **Pull Request** genera la ejecución automática del flujo de
integración y despliegue.
- Validación de parámetros y entornos (`develop`, `production`).

------------------------------------------------------------------------

##  Despliegue en Producción

-   Duplicación de estructura para múltiples regiones.
-   Configuración de parámetros de entorno en los Jobs.
-   Ejecución del pipeline desde **GitHub Actions**, con correcciones
    iterativas en catálogos y esquemas.
-   Validación de éxito del workflow y creación de tablas `bronze`,
    `silver`, `golden`.

Visualización de los archivos **Delta Parquet** en Azure CLI y
confirmación de la data migrada correctamente.

------------------------------------------------------------------------

##  Disponibilización de Data en Azure Database

Desde el workspace `prod_ecommerce` se creó un notebook para **cargar la
data Golden** hacia **Azure SQL Database** (`ecommerce`) mediante
DataFrames.
Esta capa se emplea como **fuente principal para el análisis BI**.

------------------------------------------------------------------------

##  Dashboard en Power BI

-   Conexión directa con **Azure SQL Database**.
-   Importación de la tabla `sales_orders_gold`.
-   Validación de consistencia y exploración inicial de datos.
-   Creación de dashboard con indicadores clave de negocio:
    -   Ventas por categoría.
    -   Efectividad de campañas.
    -   Segmentación de clientes.
    -   Análisis de descuentos vs. ventas.
 


<img width="523" height="259" alt="image" src="https://github.com/user-attachments/assets/a81dd860-b870-4e22-891b-de9a60bed44f" />




------------------------------------------------------------------------

##  Resultados

-   ETL implementado y validado de extremo a extremo.
-   Proceso CI/CD automatizado.
-   Datos disponibles en Azure SQL Database.
-   Dashboard analítico operativo en Power BI.
-   Arquitectura modular, escalable y segura basada en Azure +
    Databricks.

------------------------------------------------------------------------

##   Tecnologías Utilizadas

-   **Microsoft Azure**
    -   Azure Storage Account
    -   Azure Databricks
    -   Azure SQL Database
-   **Databricks**
    -   PySpark / SQL
    -   Delta Lake / Unity Catalog
-   **GitHub Actions** (CI/CD)
-   **Power BI**
-   **Python**

------------------------------------------------------------------------

##  Estructura del Proyecto

    /ecommerce/
    ├── develop/
    │   ├── notebooks/
    │   │   ├── extract.ipynb
    │   │   ├── transform.ipynb
    │   │   └── load.ipynb
    │   └── workflows/
    │       └── etl_job.json
    ├── production/
    │   ├── scripts/
    │   │   └── main/
    │   └── config/
    │       └── parameters.json
    ├── data/
    │   └── Ecommerce_Sales_Prediction_Dataset.csv
    └── .github/
        └── workflows/
            └── script.yml

------------------------------------------------------------------------

##  Autor

**Ing. Rubén Soria**\
Data Engineer\
📧 *\[ruben.soria@outlook.com]*\
💼 *\[LinkedIn: https://www.linkedin.com/in/rubensoria-sys/]*
