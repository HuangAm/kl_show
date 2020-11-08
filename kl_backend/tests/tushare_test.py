# 一次性获取全部日k线数据
# all_k_data = ts.get_hist_data('600848')
# print(all_k_data)


# 实时分笔
# df = ts.get_realtime_quotes('000581')  # Single stock symbol
# print(df)


# 当日分笔
# df = ts.get_today_ticks('sh')
# print(df)

# df = ts.get_tick_data('600848')
# print(df)


# 实时行情(所有股票)
# today_all = ts.get_today_all()
# print(today_all)

# xx = ts.get_tick_data('sh')
# print(xx)


# 实时行情(当前股票),highstock版
# one_current = ts.get_realtime_quotes('601333')  # 返回 Dataframe
# dic = {}
# dic['open'] = one_current['open'][0]
# dic['high'] = one_current['high'][0]
# dic['low'] = one_current['low'][0]
# dic['close'] = one_current['price'][0]
# dic['volume'] = one_current['volume'][0]
# t = one_current['date'][0] + ' ' + one_current['time'][0].rsplit(':',1)[0]
# dic['time'] = time.mktime(time.strptime(t, '%Y-%m-%d %H:%M'))
# dic['name'] = one_current['name'][0]
# dic['code'] = one_current['code'][0]
# print(dic)

# 历史k线数,highstock版
# k_his_data = ts.get_hist_data('600848', start='2019-01-01', ktype='5')  # 获取天k线数据
# data = []
# for i in k_his_data.index:
#     dic = {}
#     ts = time.mktime(time.strptime(i, '%Y-%m-%d'))
#     dic['time'] = ts
#     dic['open'] = k_his_data['open'][i]
#     dic['high'] = k_his_data['high'][i]
#     dic['low'] = k_his_data['low'][i]
#     dic['close'] = k_his_data['close'][i]
#     dic['volume'] = k_his_data['volume'][i]
#     data.append(dic)

# ['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change', 'ma5', 'ma10', 'ma20',
# 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']
# k_his_data = ts.get_hist_data('600000', start='2019-04-30', ktype='15')  # 获取天k线数据
# k_his_data.to_csv('xx.csv')
# data = []
# for i in k_his_data.index:
#     data_one_day = []
#     data_one_day.append(i)  # 时间
#     data_one_day.append(k_his_data['open'][i])
#     data_one_day.append(k_his_data['close'][i])
#     data_one_day.append(k_his_data['price_change'][i])
#     data_one_day.append(k_his_data['p_change'][i])
#     data_one_day.append(k_his_data['low'][i])
#     data_one_day.append(k_his_data['high'][i])
#     data.append(data_one_day)
#
# import json
# f = open('xx.json', 'w', encoding='utf-8')
# s = json.dump(data, f)

# ['2015/12/31','3570.47','3539.18','-33.69','-0.94%','3538.35','3580.6','176963664','25403106','-']
# 查询当前所有正常上市交易的股票列表,写入文件
# pro = ts.pro_api(token='3be7af1cd984a528b42be617e29216d22bf47cdbd4d7abeddecdc2bc')
# data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# name_code = []
# for i in data.index:
#     name_code.append(''.join([data['name'][i], '(', data['ts_code'][i], ')']))
# data['name_code'] = name_code
# data.to_csv('stock_list.csv', index=False)
# print(data)
# import pandas as pd

# df = pd.read_csv('stock_list.csv', dtype={'symbol': str, 'list_date': str})
# print(df[df['ts_code'].str.contains(r'6000')])
# print(df)
# x = df[df.name.str.contains('浦发')]
# y = df[df.ts_code.str.contains('浦发')]
# y = df[df.name_code.str.contains('浦发')]
# print(y.empty)
# print(dict(zip(x.symbol, x.name+'('+x.ts_code+')')))
# print(y)
# print

# asset_code = self.get_argument('asset_code', 'sh')
# one_current = ts.get_realtime_quotes('sh')
# print(one_current)

# df = ts.get_tick_data('600848',src='tt')
# print(df)
# df = ts.get_today_ticks('601333')
# print(df)
import pandas as pd

# k_his_data = ts.get_hist_data(code='sh', ktype='5')  # 调用tushare接口
# for ma in [5, 35]:
#     k_his_data['MA_' + str(ma)] = pd.DataFrame.rolling(k_his_data['close'], ma).mean()
# k_his_data.to_csv('sh.csv')
# if not k_his_data.empty:
#     data = []  # echarts 需要的数据
#     for i in k_his_data.index:
#         data_one_day = []
#         data_one_day.append(i)  # 时间
#         data_one_day.append(k_his_data['open'][i])  # 开盘价
#         data_one_day.append(k_his_data['close'][i])  # 收盘价
#         data_one_day.append(k_his_data['price_change'][i])  # 价格变动
#         data_one_day.append(k_his_data['p_change'][i])  # 涨跌幅
#         data_one_day.append(k_his_data['low'][i])  # 最低价
#         data_one_day.append(k_his_data['high'][i])  # 最高价
#         if k_his_data['MA_5'][i] > k_his_data['MA_35'][i]:
#             data_one_day.append(1)  # 金叉
#         # elif k_his_data['MA_5'][i] <= k_his_data['MA_35'][i]:
#         #     data_one_day.append(0)  # 死叉
#         else:
#             data_one_day.append(0)  # 死叉
#         print(data_one_day)
#         data.append(data_one_day)


# query_str = '600'
# if query_str:
#     df = pd.read_csv('stock_list.csv', dtype={'symbol': str, 'list_date': str})
#     df_filter_name_code = df[df.name_code.str.contains(query_str)]  # df.name_code.str.contains
#     data = [{'code':k, 'name':v} for k,v in zip(df_filter_name_code.symbol, df_filter_name_code.name_code)]
#     print(data)

query_str = '创业'
df1 = pd.DataFrame({'symbol': ['sh', 'sz', 'hs300', 'sz50', 'zxb', 'cyb'],
                    'name_code': ['上证指数(000001.SH)', '深圳成指(39901.SZ)', '沪深300(000300.SH)', '上证50(000016.SH)',
                                  '中小板指(399005.SZ)', '创业板指(399006.SZ)']}, index=None)
df_filter_name_code = df1[df1.name_code.str.contains(query_str)]
print(df_filter_name_code)