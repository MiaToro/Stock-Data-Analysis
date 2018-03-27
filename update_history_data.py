from classesfd.StockData import StockData

TestStockData = StockData()

symbols = ['NFLX', '0700.HK', 'ALGN', 'AMZN']

for i, symbol in enumerate(symbols[0:2]):
    xx = TestStockData.merge_web_his_data_to_all(symbol)
    print(xx)

# yy = TestStockData.read_csv_file('0700.HK')
# print(yy)