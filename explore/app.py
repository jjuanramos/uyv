import marimo

__generated_with = "0.9.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __():
    import marimo as mo
    import polars as pl
    import dlt
    import requests
    import httpx
    import duckdb
    return dlt, duckdb, httpx, mo, pl, requests


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Resumen

        - Explorar API de INE
        - Conseguir consumir de forma programática del [IPV (Índice de Precios de Vivienda)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607)
              - `{"Id":15, "Cod_IOE":"30457", "Nombre":"Índice de Precios de la Vivienda (IPV)", "Codigo":"IPV"}`
        - Fuente: [David Gasquez](https://github.com/davidgasquez/dine/blob/main/ine.ipynb).

        Entonces:

        - Tenemos los [Índices de Precios de Vivienda](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607). Para saber el id de una tabla, todo lo que tenemos que hacer es clicar en "Tablas más consultadas...", ahí vemos las tablas, que en su url (para Índices por CCAA: general, vivienda nueva y de segunda mano
        , su url es https://www.ine.es/jaxiT3/Tabla.htm?t=25171). Ahí, el ID es 25171.

        - Para obtener los datos de esa tabla con ese ID, accedemos a la API a través de "https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/25171?det=1". Los parámetros posibles en la llamada a la API están [aquí](https://www.ine.es/dyngs/DataLab/manual.html?cid=47).

         No obstante, la forma más viable es simplemente llamando al csv con separador ";"

        ```
        pl.read_csv("https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/25171.csv", separator=";")
        ```
        """
    )
    return


@app.cell
def __(httpx):
    INE_BASE_URL = "https://servicios.ine.es/wstempus/js/ES"

    client = httpx.Client(
        base_url=INE_BASE_URL,
        limits=httpx.Limits(max_keepalive_connections=20),
        transport=httpx.HTTPTransport(retries=3),
    )

    def ine_request(client: httpx.Client, endpoint, paginate=True):
        page = 1
        data = []

        while True:
            params = {"det": 10}

            if paginate:
                params["page"] = page

            response = client.get(
                f"/{endpoint}", params=params, follow_redirects=True
            ).json()

            if not response:
                break

            data.extend(response)

            if len(response) < 500 or not paginate:
                break

            page += 1

        return data
    return INE_BASE_URL, client, ine_request


@app.cell
def __(client, ine_request, pl):
    operaciones_disponibles = pl.DataFrame(ine_request(client, "OPERACIONES_DISPONIBLES"))
    operaciones_disponibles.filter(
        pl.col("Codigo") == "IPV"
    )
    return (operaciones_disponibles,)


@app.cell
def __(client, ine_request, pl):
    # Mediante esta llamada, obtenemos todas las tablas asociadas al IPV, que tiene como ID el número 15

    def get_series_tabla_url(tabla_id):
        return (
            f"https://servicios.ine.es/wstempus/jsCache/ES/SERIES_TABLA/{tabla_id}?det=10"
        )


    def get_tablas_download_url(tabla_id):
        return f"https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/{tabla_id}.csv"


    tablas = pl.DataFrame(ine_request(client, "TABLAS_OPERACION/15"))
    tablas = tablas.with_columns(
        pl.col("Id")
        .map_elements(get_series_tabla_url, return_dtype=pl.String)
        .alias("series_tabla_url"),
        pl.col("Id")
        .map_elements(get_tablas_download_url, return_dtype=pl.String)
        .alias("tablas_download_url"),
    )
    tablas
    return get_series_tabla_url, get_tablas_download_url, tablas


@app.cell
def __(tablas):
    with open("series.input.spec", "w") as f:
        for t in tablas.rows(named=True):
            f.write(f"{t['series_tabla_url']}\n")
            f.write("\tout=series_metadata.json\n")
            f.write(f"\tdir=dataset/tablas/{t['Id']}\n\n")

    with open("tablas.input.spec", "w") as f:
        for t in tablas.rows(named=True):
            f.write(f"{t['tablas_download_url']}\n")
            f.write(f"\tout={t['Id']}.csv\n")
            f.write(f"\tdir=dataset/tablas/{t['Id']}\n\n")
    return f, t


@app.cell
def __():
    import subprocess

    series_result = subprocess.run(
        [
            "aria2c",
            "-i",
            "series.input.spec",
            "-j",
            "50",
            "-x",
            "16",
            "-s",
            "8",
            "-c",
            "--file-allocation=none",
            "--console-log-level=warn",
        ],
        capture_output=True,
        text=True,
    )
    return series_result, subprocess


@app.cell
def __(subprocess):
    result = subprocess.run(
        ["grep", "-rl", "unos minutos", "dataset/tablas"],
        capture_output=True,
        text=True,
    )

    missing_metadata_files = result.stdout.splitlines()

    print(f"Missing metadata files: {len(missing_metadata_files)}")
    return missing_metadata_files, result


@app.cell
def __(subprocess):
    tablas_result = subprocess.run(
        [
            "aria2c",
            "-i",
            "tablas.input.spec",
            "-j",
            "50",
            "-x",
            "16",
            "-s",
            "8",
            "-c",
            "--file-allocation=none",
            "--console-log-level=warn",
            "--allow-overwrite=true",
        ],
        capture_output=True,
        text=True,
    )
    return (tablas_result,)


@app.cell
def __(client, ine_request, pl):
    df = pl.DataFrame(ine_request(client, "SERIES_TABLA/25171"))

    return (df,)


@app.cell
def __(p):
    df = p
    return (df,)


@app.cell
def __(df):
    df.head()
    return


@app.cell
def __(pl):
    newdf = pl.read_csv("dataset/tablas/25171/25171.csv", separator=";")
    newdf.head()
    return (newdf,)


@app.cell
def __(pl):
    test = pl.read_csv("https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/25171.csv", separator=";")
    test.head()
    return (test,)


@app.cell
def __(mo):
    mo.md(
        r"""

        import os

        os.makedirs("dataset", exist_ok=True)

        tablas = pl.json_normalize(t)
        print(tablas.shape)
        tablas.write_ndjson("dataset/tablas.jsonl")
        tablas.sample(5)
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
