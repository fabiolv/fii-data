# fii-data
Small Flask API that scrapes the [FIIS.com.br](https://www.fiis.com.br/) site to get FII data.
This is mainly to be used as a data source in Google Sheets.

The data is gathered from the URL below:
https://fiis.com.br/{TICKER}/

API Usage:

/fii/<TICKER>[?format=XML]

The default response is a JSON like below:

```
{
  "ticker": "VRTA11",
  "name": "FATOR VERITA",
  "price": "104.70",
  "value_per_share": "97.03"
}
```

If the `format=XML` option is passed, then the response is converted to XML.

The `Procfile` included let it run in Heroku as a web app. But also, a `Dockerfile` is provided to let it be built as a Docker image where needed.