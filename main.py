import yfinance as yf

def fetch_company_info(company_id):
  ticker = yf.Ticker(f"{company_id}.T")
  ticker_info = ticker.info

  print(f"企業名: {ticker_info['longName']}")
  current_price = "{:,}".format(ticker_info['currentPrice'])
  print(f"現在値: { current_price }円")
  return

def main():
  print("start")

  # 9984: Softbank group, T: 東証
  # 7974: Nintendo
  company_ids = [9984, 7974]

  # fetch each company info
  for company_id in company_ids:
    fetch_company_info(company_id)

  print("end")

if __name__ == '__main__':
  main()
