# fii-fundamentus
Small Flask API that scrapes the [Fundamentus](https://www.fundamentus.com.br/) site to get FII data.
This is mainly to be used as a data source in Google Sheets.

The data is gathered from the URL below:
https://www.fundamentus.com.br/detalhes.php?papel={TICKER}

API Usage:

/fii/<TICKER>[?format=XML]

The default response is a JSON like below:

```
{
    "name": "FUNDO DE INVESTIMENTO IMOBILIARIO IRIDIUM RECEBIVEIS IMOBILIARIOS",
    "price": "110.10",
    "total_shares": "33044581",
    "net_worth": "3240390000",
    "value_per_share": "98.06",
    "dividends_12m": "10.97",
    "dividend_yield": "12.5%",
    "PVP": 1.12
}
```

If the `format=XML` option is passed, then the response is converted to XML.

The `Procfile` included let it run in Heroku as a web app. But also, a `Dockerfile` is provided to let it be built as a Docker image where needed.