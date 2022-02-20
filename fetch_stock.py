import yfinance as yf

def fetch_company_info(response_body, company_id):
  ticker = yf.Ticker(f"{company_id}.T")
  ticker_info = ticker.info

  response_body.append(f"企業名: {ticker_info['longName']}")
  current_price = "{:,}".format(ticker_info['currentPrice'])
  response_body.append(f"現在値: { current_price }円")
  return

def fetch_stock():
  # 9984: Softbank group, T: 東証
  # 7974: Nintendo
  company_ids = [9984, 7974]
  response_body = []

  # fetch each company info
  for company_id in company_ids:
    fetch_company_info(response_body, company_id)

  return '\n'.join(response_body)
