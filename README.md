## Context

El IPV es un indicador trimestral que tiene como principal objetivo medir la evolución
del nivel de los precios de compraventa de las viviendas de precio libre, tanto
nuevas como de segunda mano, a lo largo del tiempo. Se trata, por tanto, de un
indicador concebido únicamente para establecer comparaciones en el tiempo.

No entra dentro del ámbito del mismo la medición de los niveles de precios. De modo
que, no se podrán establecer comparaciones espaciales de los niveles de precios,
aunque sí de sus evoluciones.

El sistema de cálculo del IPV está basado en la combinación de dos elementos
básicos que reflejan las características del mercado inmobiliario, y que son
esenciales en el cálculo de los índices de precios: los precios de las viviendas, que
representan la confluencia de la oferta y la demanda del mercado, y las
ponderaciones, o importancia relativa de cada tipología de vivienda según el valor de
compra.

A partir de 2016, el periodo de referencia de las ponderaciones son los dos años anteriores.

sql
```
select distinct
    valor,
    indice_tasa,
    quarter,
    year
from base.table25171
where year in (2015, 2016, 2017, 2018)
    and tipo_vivienda = 'General'
    and comunidad_autonoma = '13 Madrid, Comunidad de'
    and indice_tasa = 'Variación trimestral'
order by year, quarter, indice_tasa desc
```

## TODO:

- [ ] Explore XMR Charts with table25171
