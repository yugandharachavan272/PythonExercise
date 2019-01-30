import requests
import logging
import sys
import json
import datetime
import xlwt
import xlsxwriter
import DBOperations as DB


def getCompanyStockExchange():
    try:
        logging.basicConfig(format='%(levelname)-10s: %(message)s', filename='webAPI.log', filemode='w', level=logging.DEBUG)
        api_key = "rbzVYGZTS_iR1fNo_Fvx"
        share_names = ['BOM531219', 'BOM500209', 'BOM530801', 'BOM538578', 'BOM538577', 'BOM538729', 'BOM539140', 'BOM539139',
                       'BOM538980', 'BOM500770']
        # share_names = ['BOM500209']
        dataset = {}
        companyData = []
        for i in share_names:
            url = 'https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}'.format(i, api_key)
            response = requests.get(url)
            if response.status_code != 200:
                logging.error('ERROR: response type {}'.format(response))
                sys.exit(1)

            content = json.loads(response.content)
            # logging.info('Company name: {}'.format(content['dataset']['name'])
            # print content
            companyName = content['dataset']['name']
            symbol = content['dataset']['dataset_code']
            data = content['dataset']['data']
            if len(data) > 0:
                lastBusinessDate = data[0][0]
                lastBusinessDateTurnOver = data[0][8]
                secondLastBusinessDate = data[1][0]
                secondLastBusinessDateTurnOver = data[1][8]
                difference = lastBusinessDateTurnOver - secondLastBusinessDateTurnOver
                obj = dict()
                obj["companyName"] = companyName
                obj["symbol"] = symbol
                obj["lastBusinessDate"] = lastBusinessDate
                obj["secondLastBusinessDate"] = secondLastBusinessDate
                obj["lastBusinessDateTurnOver"] = lastBusinessDateTurnOver
                obj["secondLastBusinessDateTurnOver"] = secondLastBusinessDateTurnOver
                obj["difference"] = difference
                # print obj
                # companyData = dataset[data]
                companyData.append(obj)
            else:
                print "No data for ", companyName
        else:
            print "Retriving Company data done"
            # Create a workbook and add a worksheet
            filename = "python_excel_test.xlsx"
            # excel_file = xlsxwriter.Workbook()
            excel_file = xlsxwriter.Workbook(filename)
            # Light red fill with dark red text.
            format_red_color = excel_file.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

            format_green_color = excel_file.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
            sheet2 = excel_file.add_worksheet('Company Stock Exchange')
            row = 0
            col = 0
            xf = 0
            # sheet2.write(row, col, value)
            rowCount = 0
            sheet2.write(rowCount, 0, "Company Name")
            sheet2.write(rowCount, 1, "Symbol")
            sheet2.write(rowCount, 2, "Last Business Date")
            sheet2.write(rowCount, 3, "Second Last BusinessDate")
            sheet2.write(rowCount, 4, "Profit/Loss")
            rowCount = 1
            dataForDBOperations = []
            for i in companyData:
                value = i['companyName']
                companyTuple = [value]
                sheet2.write(rowCount, 0, value)
                value = i['symbol']
                companyTuple.append(value)
                sheet2.write(rowCount, 1, value)
                value = i['lastBusinessDate']
                sheet2.write(rowCount, 2, value)
                companyTuple.append(value)
                value = i['secondLastBusinessDate']
                sheet2.write(rowCount, 3, value)
                companyTuple.append(value)
                value = i['difference']
                sheet2.write(rowCount, 4, value)
                if value < 0:
                    companyTuple.append(False)
                else:
                    companyTuple.append(True)
                companyTuple.append(value)
                dataForDBOperations.append(tuple(companyTuple))
                rowCount += 1
            # excel_file.save(filename)
            ColumnRange = 'E2:E{}'.format(rowCount)
            # Write a conditional format over a range.
            sheet2.conditional_format(ColumnRange, {'type': 'cell', 'criteria': '>', 'value': 0, 'format': format_green_color})
            # Write a conditional format over a range.
            sheet2.conditional_format(ColumnRange, {'type': 'cell', 'criteria': '<=', 'value': 0, 'format': format_red_color})
            excel_file.close()

            # CALL FOR DB OPERATIONS
            if len(dataForDBOperations) > 0:
                DB.save_company_stock_exchange_data(dataForDBOperations)
            else:
                print "No Company Data"

    except Exception as E:
        print "Exception : ", E
    finally:
        print "File Created Successfully..."
        pass


def get_db_data():
    db_data = DB.get_company_stock_exchange_data()
    print db_data


getCompanyStockExchange()
get_db_data()
