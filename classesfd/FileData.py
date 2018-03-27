# get data from files in the local computer

import sys
from openpyxl import load_workbook
from pandas import DataFrame
import csv

class FileData():

    files_root_path = '/datacenter/'

    def __init__(self, path=''):
        print('FileData Init')
        if path != '':
            self.files_root_path = path

    def read_txt_file(self, filename):

        with open(self.files_root_path + filename) as file:
            data = file.read()

        data_1 = data.split('\n')
        data_2 = data_1[0:(len(data_1) - 1)]

        return data_2

    def read_csv_file(self, filename):
        path = self.files_root_path + filename + '.csv'

        with open(path, 'rt') as f:
            reader_1 = csv.reader(f)
            list_one = list(reader_1)

        return list_one

    # txt, csv
    # if the file doesn't exist, create the file
    def create_write_file(self, filename, list_data, path=''):

        if path == '':
            path = self.files_root_path

        success = 1
        try:
            file = open(path + filename, 'w')
            print(path + filename)
            for row in list_data:
                for i, col in enumerate(row):
                    # print(col)
                    if i == (len(row) - 1):
                        file.write(str(col) + '\r\n')
                    else:
                        file.write(str(col) + ", ")
            file.close()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            file.close()
            return 0
        except:
            file.close()
            print("Unexpected error:", sys.exc_info()[0])
            raise
            return 0

        return success

    def read_from_xlsx(self, filename, path=''):
        if path == '':
            path = self.files_root_path

        # get data from file to DataFrame of pandas

        fpath = path + filename
        wb = load_workbook(filename=fpath)
        # sheet_ranges = wb['Activities']
        ws = wb.active

        df1 = DataFrame(ws.values)

        return df1

    # if the file doesn't exist, create the file
    def create_write_to_xlsx(self, data, cols, filename, path=''):
        success = 1
        if path == '':
            path = self.files_root_path

        file_path = path + filename  # '/datacenter/calendarlist.xlsx'
        print(file_path)
        try:
            df = DataFrame.from_records(data, columns=cols)
            df.to_excel(file_path, sheet_name='sheet1', index=False)
        except IOError as e:
            success = 0
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return success
        except ValueError as e:
            success = 0
            print("Value error")
            return success
        except:
            success = 0
            print("Unexpected error:", sys.exc_info()[0])
            raise
            return success

        return success


    # name mangling ?? but it looks useless
    # __create_write_file = create_write_file