---
title: Welcome to Evidence
---

<Details title='How to edit this page'>

  This page can be found in your project at `/pages/index.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>

```sql comunidades
 select distinct comunidad_autonoma from table25171
```

<Dropdown data={comunidades} name=comunidad value=comunidad_autonoma>
    <DropdownOption value="%" valueLabel="All Communities"/>
</Dropdown>

<Dropdown name=year>
    <DropdownOption value=% valueLabel="All Years"/>
    <DropdownOption value=2019/>
    <DropdownOption value=2020/>
    <DropdownOption value=2021/>
    <DropdownOption value=2022/>
    <DropdownOption value=2023/>
    <DropdownOption value=2024/>
</Dropdown>

```sql orders_by_category
  select 
      periodo,
      sum(valor) as valor
  from table25171
  where comunidad_autonoma like '${inputs.comunidad.value}'
  -- and date_part('year', order_datetime) like '${inputs.year.value}'
  group by periodo
  order by valor desc
```

<BarChart
    data={orders_by_category}
    title="Sales by Month, {inputs.periodo.label}"
    x=periodo
    y=valor
/>

## What's Next?
- [Connect your data sources](settings)
- Edit/add markdown files in the `pages` folder
- Deploy your project with [Evidence Cloud](https://evidence.dev/cloud)

## Get Support
- Message us on [Slack](https://slack.evidence.dev/)
- Read the [Docs](https://docs.evidence.dev/)
- Open an issue on [Github](https://github.com/evidence-dev/evidence)
