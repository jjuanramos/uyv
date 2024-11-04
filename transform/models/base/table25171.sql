MODEL (
    name base.table25171,
    kind FULL,
    cron '@daily',
    grain id
  );

with variacion_trimestral as (
  select
    md5(
        concat(
            total_nacional,
            comunidad_autonoma,
            tipo_vivienda,
            indice_tasa,
            periodo
        )
    ) as id,
    total_nacional,
    comunidad_autonoma,
    indice_tasa,
    tipo_vivienda,
    cast(substr(periodo, 1, 4) as int) as year,
    cast(substr(periodo, 6, 1) as int) as quarter,
    valor
  from
    base.table25171_raw
)

select * from variacion_trimestral