MODEL (
    name marts.xmr_25171,
    kind FULL,
    cron '@daily',
    grain id
  );

with base as (
  select
    id,
    make_date(year, (quarter * 3), 1) as index_date,
    valor as variacion_trimestral
  from base.table25171
  where indice_tasa = 'Variación trimestral'
    and tipo_vivienda = 'General'
    and comunidad_autonoma = '13 Madrid, Comunidad de'
)

select * from base;

-- copy marts.xmr_25171 to 'xmr_25171.csv'
-- with (format = 'csv');
