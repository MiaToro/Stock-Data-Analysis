from classesfd.StockData import StockData
from classesfd.StockCharts import StockCharts
from classesfd.WebData import WebData
import pandas as pd
import time
from datetime import tzinfo, timedelta, datetime

# print(datetime.now())
# # print(datetime.tzinfo())
# print(datetime.utcnow())
#
# str_utc = datetime.utcnow().strftime('%Y-%m-%d')
#
# # str_date = str(str_utc.year) + '-' + str(str_utc.month) + '-' + str(str_utc.day)
#
# print(str_utc)
# print(datetime.utcnow().strftime('%b %d %Y - %H:%M:%S'))
# print(datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))

# str = 'Mar 26 2018'
# print(str)
#
# str_date = datetime.strptime(str, '%b %d %Y')
#
# str_1 = datetime.strftime(str_date, '%Y-%m-%d')
#
# print(str_1)
# print(type(str_1))

# str = '1,495.56'
# print(str.replace(",", ""))

# print(str.replace("is", "was", 4))

# TestClass = WebData()
#
# txt = TestClass.get_CAD_USD_exchange_rate_by_date('2018-03-25')
# print(txt)

# TestClass = FileData()
#
# list_data = ['66.25', '333', '333', '1', 1234.5]
# print(TestClass.create_write_file('test.xlsxx', list_data))

# data =  [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 21}]
# data =  [{1, 211}, {5, 11, 21}]
# cols = ['a', 'b', 'c']
#
# print(TestClass.create_write_to_xlsx(data, cols, 'test.xlsx1', path=''))

# x = TestStockData.create_write_file('3test.xlsxx', list_data)
# print(x)

# yy_1 = TestStockData.get_current_stockdata_from_yahoo('0700.HK')
#
# # for i, col in enumerate(yy_1):
# #     print(i)
# #     print(col)
#
# yy = TestStockData.get_history_stockdata_from_yahoo('0700.HK')
#
# # for i, col in enumerate(yy):
# #     print(i)
# #     print(col)
#
# TestStockChart = StockCharts()
#
# TestStockChart.get_chart_for_each_year('0700.HK')

#
# xx = TestStockData.get_eps_report_from_tmxmoney('ALGN:US')
#
# print(xx)

# time_1 = time.strptime("30 Nov 00", "%d %b %y")
#
# print(time_1)
#
# print(time_1.tm_mon, time_1.tm_mday, time_1.tm_year)

# time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)