from lxml import html
import requests


# get data from webpages in the local computer

class WebData():
    symbol = ''
    url_yahoo = 'https://ca.finance.yahoo.com/quote/' + symbol + '/history?p=' + symbol
    url_currency_rate = 'https://x-rates.com/historical/?from=USD&amount=1&date='  # + date, e.g.: 2018-03-25
    url_tmxmoney_eps = 'https://web.tmxmoney.com/earnings.php?qm_symbol='  # + symbol  e.g.:DOL, AMZN:US

    def __init__(self):
        pass

    def get_webpage(self, url):

        page = requests.get(url)
        # webpage text version
        page_txt = page.text

        return page_txt

    def remove_webpage_top(self, page_txt, str='', n = 2):

        web_txt = page_txt.split(str)

        return web_txt[n]

    def remove_webpage_tail(self, page_txt, str=''):

        web_txt = page_txt.split(str)

        return web_txt[0]

    def get_split_txt(self, symbol):

        txt = 'Currency in USD'

        if symbol.find('.') != -1:
            tmp_1 = symbol.split('.')
            if tmp_1[1] == 'HK':
                txt = 'Currency in HKD'
            if tmp_1[1] == 'TO':
                txt = 'Currency in CAD'
        return txt

    def remove_webpage_top_and_tail(self, symbol):

        self.symbol = symbol
        self.url_yahoo = 'https://ca.finance.yahoo.com/quote/' + self.symbol + '/history?p=' + self.symbol

        print('url = ', self.url_yahoo)

        page_txt = self.get_webpage(self.url_yahoo)
        split_txt = self.get_split_txt(symbol)
        page_txt_1 = self.remove_webpage_top(page_txt, split_txt, 2)
        page_txt_2 = self.remove_webpage_tail(page_txt_1, '*Close price adjusted for splits.')

        return page_txt_2

    def get_CAD_USD_exchange_rate_by_date(self, str_date):

        url_currency_rate = 'https://x-rates.com/historical/?from=USD&amount=1&date=' + str_date
        print(url_currency_rate)
        page_txt = self.get_webpage(url_currency_rate)

        page_without_top = self.remove_webpage_top(page_txt, str='Canadian Dollar')
        page_mid = self.remove_webpage_tail(page_without_top, str='</a>')
        rate_by_date = page_mid.split("to=CAD'>")[1]

        return rate_by_date

    # used by 'get_eps_report_from_tmxmoney()' function
    def get_data_for_one_eps_row(self, row, str_split = '<td'):

        tmp_1 = row.split(str_split)
        tmp_2 = tmp_1[1:]

        # 0, Fiscal_Quarter_End, 1, Date, 2, Earnings_Per_Share, 3, Consensus_EPS_Forecast,
        # 4, Surprise
        eps = []

        # tags on first line
        if str_split == '<th':
            for i, row in enumerate(tmp_2):
                tmp_3 = row.split('>') [1]
                tmp_4 = tmp_3.split('<')[0]
                tmp_5 = tmp_4.replace(' ', '_')
                eps.append(tmp_5)
        else:
            for i, row in enumerate(tmp_2[0:-1]):
                tmp_s_1 = row.split('>') [1]
                tmp_s_2 = tmp_s_1.split('<')[0]
                eps.append(tmp_s_2)
            tmp_s_3 = tmp_2[-1].split('<span')[1:3]
            surprise = []
            for j, col in enumerate(tmp_s_3):
                tmp_p_1 = col.split('>')[1].split('<')[0].replace('(', '')
                surprise.append(tmp_p_1.replace(')', ''))
            eps.append(surprise)

        return eps

    def get_eps_report_from_tmxmoney(self, symbol):

        url_tmxmoney_eps = 'https://web.tmxmoney.com/earnings.php?qm_symbol=' + symbol  # e.g.:DOL, AMZN:US
        print(url_tmxmoney_eps)

        page_txt = self.get_webpage(url_tmxmoney_eps)

        page_1 = self.remove_webpage_top(page_txt, 'Earnings History', 1)
        page_2 = self.remove_webpage_tail(page_1, 'More Corporate Earnings')

        # print('page_2 = ', page_2 , '\r\n')

        page_3 = page_2.split('<tr')
        page_4 = page_3[1:-1]

        eps_list = []

        for i, row in enumerate(page_4[0:]):
            if i == 0:
                tmp_eps_1 = self.get_data_for_one_eps_row(row, '<th')
                eps_list.append(tmp_eps_1)
            else:
                tmp_eps_2 = self.get_data_for_one_eps_row(row)
                eps_list.append(tmp_eps_2)

# ['Fiscal_Quarter_End', 'Date', 'Earnings_Per_Share', 'Consensus_EPS_Forecast', 'Surprise']
# ['Q1 2018', '04/26/18', '--', '0.98', ['--', '--']]
# ['Q4 2017', '01/30/18', '1.19', '0.96', ['0.23', '23.96%']]

        return eps_list