# Reversion de tablas y files (deltas)

dbutils.widgets.removeAll()


# preparación de parametros
schemas_list = ["bronze","silver","golden"]

dbutils.widgets.text("catalog", "prod_ecommerce")
dbutils.widgets.text("storage_account","prod_adlsecommerce")

catalog_param = dbutils.widgets.get("catalog")
storage_account = dbutils.widgets.get("storage_account")


# funciones a usar
def delete_folders(path):
    try:
        dbutils.fs.rm(path, recurse=True)
        print(f"Folder {path} eliminado.")
    except Exception:
        print(f"No existe folder: {path}")
        pass


def drop_schema(schema):
    spark.sql(f"DROP SCHEMA IF EXISTS {catalog_param}.{schema} CASCADE")


spark.sql(f"USE CATALOG {catalog_param}")


# Limpieza de tablas
for schema in schemas_list:
    drop_schema(schema)

# Eliminacion del catalogo
spark.sql(f" DROP CATALOG IF EXISTS {catalog_param} CASCADE")




# Eliminar todas las carpetas de cada uno de los containers

for container in schemas_list:
    delete_folders(f"abfss://{container}@{storage_account}.dfs.core.windows.net/")
