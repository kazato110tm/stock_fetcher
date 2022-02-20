import yfinance as yf
import re

def fetch_company_info(response_body, company_id):
  ticker = yf.Ticker(f"{company_id}.T")
  ticker_info = ticker.info

  response_body.append(f"コード: {company_id}")
  response_body.append(f"企業名: {ticker_info['longName']}")
  current_price = "{:,}".format(ticker_info['currentPrice'])
  response_body.append(f"現在値: { current_price }円")
  return

def fetch_stock(input_ids):
  company_ids = re.sub(r"\s+", "", input_ids).split(',')
  response_body = []
  error_flag = False

  # fetch each company info
  for company_id in company_ids:
    if company_id.isdecimal():
      fetch_company_info(response_body, int(company_id))
    else:
      response_body.append(f"error: {company_id} is not an existing code.")
      error_flag = True

  if error_flag:
    response_body.append(f"Please enter in the following format. \n ex. 0000, 1234")

  return '\n'.join(response_body)
