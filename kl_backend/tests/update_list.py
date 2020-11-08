# 每天早上5点更新
import tushare as ts

pro = ts.pro_api(token='3be7af1cd984a528b42be617e29216d22bf47cdbd4d7abeddecdc2bc')
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
name_code = []
for i in data.index:
    name_code.append(''.join([data['name'][i], '(', data['ts_code'][i], ')']))
data['name_code'] = name_code
data.to_csv('stock_list.csv', index=False)

import rqdatac as rq
from rqdatac import *

rq.init()
future_df = all_instruments(type='Future')  # 期货列表
order_book_id_symbol = []
for i in future_df.index:
    order_book_id_symbol.append(''.join([future_df['symbol'][i], '(', future_df['order_book_id'][i], ')']))
future_df['order_book_id_symbol'] = order_book_id_symbol
future_df.to_csv('future_list.csv', index=False)
