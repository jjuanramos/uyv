import marimo

__generated_with = "0.9.9"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import polars as pl
    import dlt
    import requests
    return dlt, mo, pl, requests


@app.cell
def __(mo):
    mo.md(
        r"""
        # TODO

        - Explorar API de INE
        - Conseguir consumir de forma programática del [IPV (Índice de Precios de Vivienda)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607)
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
