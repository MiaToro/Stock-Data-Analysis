from classesfd.StockData import StockData
from matplotlib import pyplot as plt
from datetime import datetime


#

class StockCharts():
    def __init__(self):
        pass

    def get_chart_for_each_year(self, symbol):
        CStockData = StockData()
        data_his = CStockData.get_history_stockdata_from_yahoo(symbol)
        # print(data_his)

        y_start = int(data_his[1][0][0:4])
        y_end = int(data_his[-1][0][0:4])

        # print(y_start, y_end)

        yrly_data = {}
        yrly_percent = {}

        for y in range(y_start, y_end + 1):
            yrly_data[y] = []
            yrly_percent[y] = []

        # print('=======', yrly_percent)

        for i, row in enumerate(data_his[1:]):
            tmp_y = int(row[0][0:4])
            if row[4] != 'null':
                yrly_data[tmp_y].append(row[4])

        for j, col in enumerate(yrly_data):
            #    print(j, col)
            #     print(yrly_data[col])
            #     print(yrly_data[col][0])
            for k, each in enumerate(yrly_data[col]):
                tmp_p = float(each) / float(yrly_data[col][0])
                yrly_percent[col].append(tmp_p)

        # print(yrly_percent)

        # draw each year's history data line in chart
        for j in yrly_percent:
            # print(j, yrly_data[j])
            ind_x = []
            # print('len = ', len(yrly_data[j]))
            for i in range(0, len(yrly_percent[j])):
                ind_x.append(i)

            # print(ind_x)

            plt.plot(ind_x, yrly_percent[j], label=j)

        plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0.2)
        plt.show()

    def get_one_year_prediction_chart(self, symbol):

        pass

    def get_eps_price_chart(self, symbol, country='US', coefficient=25):

        C_StockData = StockData()
        s_eps = C_StockData.get_eps_report_from_tmxmoney(symbol + ':' + country)

        x_date = []
        y_eps_quarterly = []
        for i, row in enumerate(s_eps[1:]):
            if row[2] != '--':
                eps_date = datetime.strptime(row[1], '%m/%d/%y')
                x_date.append(eps_date)
                y_eps_quarterly.append(float(row[2]) * coefficient)

        plt.plot(x_date, y_eps_quarterly, '.', label='Quarterly')  #

        x_p_date = []
        y_price = []
        s_price = C_StockData.get_history_stockdata_from_yahoo(symbol)
        for j, col in enumerate(s_price[1:]):
            tmp_date = datetime.strptime(col[0], '%Y-%m-%d')
            x_p_date.append(tmp_date)
            y_price.append(col[4])

        plt.plot(x_p_date, y_price, label='Price')  # '.',

        plt.title(symbol)
        plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0.2)
        plt.show()

    def get_pe_price_chart(self, symbol, country='US', coefficient=25):

        pass
