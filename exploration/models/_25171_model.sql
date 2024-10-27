-- Model SQL
-- Reference documentation: https://docs.rilldata.com/reference/project-files/models

with model as (
  select
    "Índices y tasas" as indices_tasas,
    "Comunidades y Ciudades Autónomas" as comunidades,
    "General, vivienda nueva y de segunda mano" as general,
    "Total Nacional" as total_nacional,
    cast(left(Periodo, 4) as int) as year,
    cast(replace(total, ',', '.') as float) as index,
    right(Periodo, 2) as quarter
  from _25171
)

select * from model
where comunidades = '13 Madrid, Comunidad de'
  and indices_tasas = 'Variación trimestral'
  and general = 'General'
order by year desc, quarter

