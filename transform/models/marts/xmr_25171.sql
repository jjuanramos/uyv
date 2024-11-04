MODEL (
    name marts.xmr_25171,
    kind FULL,
    cron '@daily',
    grain id
  );

with base as (
  select * from base.table25171
)

select * from base
