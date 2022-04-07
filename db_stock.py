import csv
import pymysql
import sys
#-------functions------
def convert_str_to_list(f_string):
#converting string to list
    f_list = []
    for line in f_string.split('\n'):
        f_list.append(line.split(','))
    return f_list



#---------main-----------
ticker_str = input("Please enter ticker symbols seperated by spaces: ")
user_name = input("Please enter database user: ")
paswd = input("Please enter password: ")
ticker_list = []
for ticker in ticker_str.split(' '):
    ticker_list.append(ticker)

ticker_dic = {}

#converting all csv to string
for ticker in ticker_list:
    file_name = '{}.csv'.format(ticker)
    file = open(file_name, 'r')
    f_string = file.read()

    #converting all string to list
    f_list = convert_str_to_list(f_string)
    ticker_dic[ticker] = f_list

#connecting to mysql
db = pymysql.connect(host = 'localhost', user =user_name, password =paswd, db = 'test')
cursor = db.cursor()
#creating sql queries
query_create_table = "CREATE TABLE {} ( symbol varchar(4), dateID varchar(8) PRIMARY KEY NOT NULL, open float(8,2), high float(8,2), low float(8,2), close float(8,2), vol int(8));"
query_insert_table = "INSERT INTO {} (symbol, dateID, open, high, low, close, vol) VALUES (\'{}\',\'{}\',{},{},{},{},{})"


for ticker in ticker_dic:
    #creating a table for each ticker
    try:
        cursor.execute(query_create_table.format(ticker))
    except:
        sys.exit("Failed on creating table {}".format(ticker))
    
    #inserting row to each table
    for i in range(1, len(ticker_dic[ticker])-1 ):

        
         insert_query = query_insert_table.format(ticker,
          ticker,
          ticker_dic[ticker][i][6], 
          ticker_dic[ticker][i][1],
          ticker_dic[ticker][i][2], 
          ticker_dic[ticker][i][3], 
          ticker_dic[ticker][i][4],
          ticker_dic[ticker][i][5])

         try:
            cursor.execute(insert_query)
            #print('{}th row of {} table inserted'.format(i, ticker))
            db.commit()
         except:
             sys.exit("Failed on insert table {}".format(ticker))


print('all values filled')

