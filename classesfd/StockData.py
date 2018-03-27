from classesfd.FileData import FileData
from classesfd.WebData import WebData
from datetime import datetime

#
class StockData(WebData, FileData):

    def __init__(self):
        # print('StockData Init')
        pass

    def get_tags(self, str):

        tags = []
        tag_1 = str.split('<span')[1:]

        for i, row in enumerate(tag_1):
            tag_2 = row.split('</span>')[0].split('>')[1]
            tag_2 = tag_2.replace('*', '')
            tag_2 = tag_2.replace(' ', '_')
            tags.append(tag_2)

        return tags

    def get_one_record(self, str):

        row = []
        row_1 = str.split('<span')[1:]

        for i, col in enumerate(row_1):
            col_1 = col.split('</span>')[0].split('>')[1]
            row.append(col_1)

        return row

    def get_records(self, listdata):

        records = []

        for i, row in enumerate(listdata[0:]):
            row_1 = self.get_one_record(row)
            records.append(row_1)

        return records

    def get_current_stockdata_from_yahoo(self, symbol):
        # data example
        # first row is tags
        # 0  ['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
        # 1  ['Mar 21, 2018', '472.200', '475.600', '460.600', '462.600', '462.600', '28,243,967']

        txt_1 = self.remove_webpage_top_and_tail(symbol)
        txt_2 = txt_1.split('<tr')

        # remove the first and last items
        txt_2 = txt_2[1:-1]

        tags = self.get_tags(txt_2[0])
        records = self.get_records(txt_2[1:])

        tags_list = []
        tags_list.append(tags)
        return tags_list + records

    def get_history_stockdata_from_yahoo(self, symbol):
        # data example
        # first row is tags
        # 0  ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        # 1  ['2004-06-16', '0.875000', '0.925000', '0.815000', '0.830000', '0.751258', '2198875000']

        data_list = self.read_csv_file(symbol)

        return data_list

    def merge_web_his_data_to_all(self, symbol):
        # data example
        # first row is tags
        # 0  ['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
        # 1  ['Mar 21, 2018', '472.200', '475.600', '460.600', '462.600', '462.600', '28,243,967']
        # from new to old
        data_cur = self.get_current_stockdata_from_yahoo(symbol)
        # data example
        # first row is tags
        # 0  ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        # 1  ['2004-06-16', '0.875000', '0.925000', '0.815000', '0.830000', '0.751258', '2198875000']
        # from old to new
        data_his = self.get_history_stockdata_from_yahoo(symbol)

        last_his_date = datetime.strptime(data_his[-1][0], '%Y-%m-%d')
        # the date for the newest data in history data
        # print('last_his_date =', last_his_date)

        data_to_add = []
        index_merge_cur = ''

        for i, row in enumerate(data_cur[1:]):
            # print(i, row)
            date_cur = datetime.strptime(row[0], '%b %d, %Y')
            date_str_cur = datetime.strftime(date_cur, '%Y-%m-%d')
            if date_cur == last_his_date:
                index_merge_cur = i + 1
                break
            else:
                row[0] = date_str_cur
                row[6] = row[6].replace(',', '')
                data_to_add.append(row)

        if index_merge_cur == '':
            print('History date for ', symbol, ' need to update')

        data_to_add.reverse()
        data_all = data_his + data_to_add

        # for k, line in enumerate(data_all):
        #     print(k, line)
        success = self.create_write_file(symbol + '.csv', data_all)

        return success


    def get_eps_yearly(self, symbol):

        eps_quarterly = self.get_eps_report_from_tmxmoney(symbol)


        pass

    def get_difference_by_days(self, symbol, days, str_date):

        x_p_date = []
        y_price = []
        s_price = self.get_history_stockdata_from_yahoo(symbol)
        for j, col in enumerate(s_price[1:]):
            tmp_date = datetime.strptime(col[0], '%Y-%m-%d')
            x_p_date.append(tmp_date)
            y_price.append(col[4])


    def get_stocks_list(self):

        pass
