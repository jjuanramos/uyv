import pandas as pd
import typing as t
from datetime import datetime
from sqlmesh import ExecutionContext, model

@model( 
    "base.table25171",
    kind="full",
    columns={
        "total_nacional": "text",
        "comunidad_autonoma": "text",
        "tipo_vivienda": "text",
        "indice_tasa": "text",
        "periodo": "text",
        "valor": "float",
    }
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:
    df = pd.read_csv("https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/25171.csv", sep=";")
    df = df.rename(columns={
        'Total Nacional': 'total_nacional',
        'Comunidades y Ciudades Autónomas': 'comunidad_autonoma', 
        'General, vivienda nueva y de segunda mano': 'tipo_vivienda',
        'Índices y tasas': 'indice_tasa',
        'Periodo': 'periodo',
        'Total': 'valor'
    })
    df.valor = df.valor.replace(",", ".", regex=True)
    df.valor = df.valor.astype(float)
    return df
