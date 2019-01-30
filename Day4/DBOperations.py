import sqlite3


def save_company_stock_exchange_data(data):
    with sqlite3.connect('StockExchange') as db:
        cursor = db.cursor()
        # CREATE TABLE
        try:
            cursor.execute("""CREATE TABLE CompanyStockExchange (Id INT, CompanyName TEXT, LastBusinessDate TEXT,
             SecondLastBusinessDate TEXT, IsProfit BOOLEAN, Difference INT)""")
        except Exception as E:
            print "Error ", E
        finally:
            pass

        # GO TO SAVE DATA --
        try:
            # cursor.execute("""INSERT INTO EMP VALUES(1, 'Yugandhara', 'IT', 40000)""")
            purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                         ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                         ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                         ]
            # print data
            cursor.executemany('INSERT INTO CompanyStockExchange VALUES (?,?,?,?,?,?)', data)
        except Exception as E:
            print "Error ", E
        else:
            db.commit()
        finally:
            pass


def get_company_stock_exchange_data():
    with sqlite3.connect('StockExchange') as db:
        cursor = db.cursor()
        try:
            cursor.execute("""SELECT * FROM  CompanyStockExchange""")
        except Exception as E:
            print "Error ", E
        else:
            data = []
            for row in cursor.fetchall():
                data.append(row)
                print row
            return data
