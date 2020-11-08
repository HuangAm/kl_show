import rqdatac as rq

# from rqdatac import *

rq.init()
# 获取中国市场上所有合约的基础信息
# futures = all_instruments(type='Future')  # 期货列表
# futures.to_csv('future_list.csv', index=False)
# 期货详细信息
# future = instruments('000001.XSHE', market='cn')
# print(future)
# 期货历史行情数据
# import datetime
# t = datetime.date.today()
# print(str(t))
# xx = get_price('000001.XSHE',
#                start_date='2013-01-04',
#                end_date='2019-05-01',
#                frequency='1d',
#                fields=None,
#                adjust_type='pre',
#                skip_suspended=False,
#                market='cn')
# print(xx)
# 期货当前行情快照
# future_current = current_snapshot('CJ2003')
# print(future_current)

# 调取历史数据
# his_tick_data = rq.get_price('000001.XSHE', '2018-3-23', '2018-3-23', 'tick')
# print(his_tick_data)
# 获取财务数据
# q = query(
#     financials.income_statement.net_profit,
#     financials.announce_date
#     ).filter(
#     financials.stockcode.in_(['000002.XSHE'])
#     )
# finance_data = get_financials(q, '2016q3', '2q')
# print(finance_data)
# 获取实时数据
# current_data = current_snapshot('RB1805')
# print(current_data)
# xx = get_ticks('000001.XSHE')
# print(xx)

# 日线，分钟线
# xx = get_price('RB1805', frequency='1d')
# print(xx)
# oo = get_ticks('RB1805')
# print(oo)

# future_data = rq.get_price('SC1906', frequency='15m')
# ma = 5
# for ma in [5, 35]:
#     future_data['MA_' + str(ma)] = pd.DataFrame.rolling(future_data['close'], ma).mean()
# x.to_csv('oo.csv')
# xx = rq.get_previous_trading_date(datetime.date.today(), n=35)
# print(xx)
# future_data.to_csv('SC1906_ma_ema.csv')

# xx = pd.read_csv('SC1906_ma_ema.csv', index_col=0)

# for i in future_data.index:
#     if future_data['MA_5'][i] > future_data['MA_35'][i]:
#         print(i, '金叉')
#     elif future_data['MA_5'][i] <= future_data['MA_35'][i]:
#         print(i, '死叉')

# xx = rq.get_price('000001.XSHE', frequency='15m')
# print(xx)

futures = rq.all_instruments(type='')  # 期货列表
futures.to_csv('future_list.csv', index=False)