---
title: Welcome to Evidence
---

<Details title='How to edit this page'>

  This page can be found in your project at `/pages/index.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>

```sql query
	select
		index_date::date::text as x,
		variacion_trimestral as value
	from uyv.xmr_25171
```

<ShareLinkComponent 
  xLabel="fecha"
  yLabel="variacion trimestral"
  xdata={query} />