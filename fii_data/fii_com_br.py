import requests
from requests.models import Response
from bs4 import BeautifulSoup

class TickerNotFoundError(Exception):
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.message = f'Could not retrieve data for {self.ticker}'
        super().__init__(self.message)

class HTMLPaseError(Exception):
    def __init__(self, title) -> None:
        self.ticker = title
        self.message = f'Error parsing the HTML data of the page: {title}'
        super().__init__(self.message)

def get_html_data(ticker: str) -> Response:
    url = f'https://fiis.com.br/{ticker}'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            }

    html = requests.get(url, headers=header)
    if 'Não encontramos o que você procurava' in html.text \
            or ticker not in html.text \
            or html.status_code != 200:
        raise TickerNotFoundError(ticker)
    
    return html

def parse_html(soup:BeautifulSoup, label_elem:str, label_class:str, label_text:str, value_elem:str, value_class:str) -> str:
    vpc_label = soup.find('h3', class_='title', text='Valor Patrimonial por Cota')
    vpc_value = vpc_label.find_previous('h3', class_='value')
    vpc_value.text
        
    label = soup.find(label_elem, class_=label_class, text=label_text)
    if label is None:
        raise HTMLPaseError(soup.title.text)
    value = label.find_previous(value_elem, class_=value_class)
    if value is None:
        raise HTMLPaseError(soup.title.text)
    return value.text



# def get_total_shares(soup: BeautifulSoup) -> str:
#     shares = parse_html(soup, label_class='txt', label_text='Nro. Cotas', value_class='data w3')
#     shares = shares.replace('.', '')
#     return shares

# def get_net_worth(soup: BeautifulSoup) -> str:
#     net_worth = parse_html(soup, label_class='txt', label_text='Patrim Líquido', value_class='data w1')
#     net_worth = net_worth.replace('.', '').replace(',', '')
#     return net_worth

# def get_dividends_12m(soup: BeautifulSoup) -> str:
#     dividends = parse_html(soup, label_class='txt', label_text='Dividendo/cota', value_class='data w2')
#     dividends = dividends.replace(',', '.')
#     return dividends

# def get_dividend_yield(soup: BeautifulSoup) -> str:
#     dividend_yield = parse_html(soup, label_class='txt', label_text='Div. Yield', value_class='data')
#     dividend_yield = dividend_yield.replace(',', '.')
#     return dividend_yield

def get_price(soup: BeautifulSoup) -> str:
    price_span = soup.find('span', class_='value')
    price = price_span.text
    price = price.replace(',', '.')
    return price

def get_fund_name(soup: BeautifulSoup) -> str:
    ticker_h1 = soup.find('h1')
    name = ticker_h1.find_next('p').text.strip().upper()
    return name

def get_value_per_share(soup: BeautifulSoup) -> str:
    vps_p = soup.find('p', text='Val. Patrimonial p/Cota')
    vps_value = vps_p.find_previous('p').text
    vps = vps_value.replace('R$', '').replace(',', '.').strip()
    return vps

def get_number_investors(soup: BeautifulSoup) -> str:
    investors_p = soup.find('p', text='N° de Cotistas')
    investors = investors_p.find_previous('p').text
    investors = investors.replace('.', '')
    return investors

def get_cnpj(soup: BeautifulSoup) -> str:
    cnpj_span = soup.find('span', text='CNPJ')
    cnpj = cnpj_span.find_next('b').text
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
    return cnpj

def get_total_shares(soup: BeautifulSoup) -> str:
    shares_span = soup.find('span', text='Número de Cotas')
    shares = shares_span.find_next('b').text
    shares = shares.replace('.', '')
    return shares

def get_dy(soup: BeautifulSoup) -> str:
    dy_p = soup.find('p', text='Dividend Yield')
    dy = dy_p.find_previous('b').text
    dy = dy.replace(',', '.')
    return dy

def get_last_dividend(soup: BeautifulSoup) -> str:
    last_dividend_p = soup.find('p', text='Último Rendimento')
    last_dividend = last_dividend_p.find_previous('b').text
    last_dividend = last_dividend.replace(',', '.')
    return last_dividend

def get_fii_info(ticker: str) -> dict:
    try:
        html = get_html_data(ticker)
        html.status_code
    except TickerNotFoundError as err:
        return {'message': err.message,
                'error': True}

    try:
        soup = BeautifulSoup(html.text, features='html.parser')

        fii_info = {
            'ticker': ticker,
            'name': get_fund_name(soup),
            'price': get_price(soup),
            'value_per_share': get_value_per_share(soup),
            'investors': get_number_investors(soup),
            'cnpj': get_cnpj(soup),
            'total_shares': get_total_shares(soup),
            'dividend_yield': get_dy(soup),
            'last_dividend': get_last_dividend(soup),
        }
        # fii_info['PVP'] = round(float(fii_info['price']) / float(fii_info['value_per_share']), 2)
    except HTMLPaseError as err:
        return {'message': err.message,
                'error': True}
    
    return fii_info

if __name__ == '__main__':
    pass