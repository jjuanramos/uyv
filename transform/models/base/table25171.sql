MODEL (
    name base.table25171,
    kind INCREMENTAL_BY_TIME_RANGE (
		time_column index_date
	),
    cron '@daily',
    grain id,
    audits (
      not_null(columns := (id)),
      unique_values(columns := (id)),
    )
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
),

con_fecha as (
	select
		* except (
			year,
			quarter
		),
    	make_date(year, (quarter * 3), 1) as index_date
	from variacion_trimestral
)

select * from con_fecha
