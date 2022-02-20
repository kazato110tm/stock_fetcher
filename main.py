import yfinance as yf

def main():
  print("start")
  # 9984: Softbank group, T: 東証
  ticker_info = yf.Ticker("9984.T")
  # ticker_info.info
  print("end")

if __name__ == '__main__':
  main()
