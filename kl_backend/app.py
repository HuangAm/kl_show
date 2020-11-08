import traceback

import pandas as pd
# import rqdatac as rq
import tornado.ioloop
import tornado.web
import tornado.websocket
import tushare as ts

from log.gen_logger import logger

# rq.init()


def try_except(func):
    """
    日志装饰器
    """

    def handle_problems(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            self.write({'message': '{}'.format(e), 'status': 0})
            logger.error(traceback.format_exc())

    return handle_problems


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        """解决跨域"""
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def options(self):
        """解决复杂请求"""
        self.set_status(204)
        self.finish()


class QueryStockHandler(BaseHandler):
    """模糊查询股票信息"""

    @try_except
    def post(self):
        query_str = self.get_argument('query_str', None)
        if query_str:
            df = pd.read_csv('stock_list.csv', dtype={'symbol': str, 'list_date': str})
            df_filter_name_code = df[df.name_code.str.contains(query_str)]  # df.name_code.str.contains
            if df_filter_name_code.empty:
                df1 = pd.DataFrame({'symbol': ['sh', 'sz', 'hs300', 'sz50', 'zxb', 'cyb'],
                                    'name_code': ['上证指数(000001.SH)', '深圳成指(39901.SZ)', '沪深300指数(000300.SH)',
                                                  '上证50(000016.SH)', '中小板(399005.SZ)', '创业板(399006.SZ)']})
                df_filter_name_code = df1[df1.name_code.str.contains(query_str)]
            if df_filter_name_code.empty:
                self.write({'data': '', 'status': 200})
            else:
                data = [{'code': k, 'name': v} for k, v in
                        zip(df_filter_name_code.symbol, df_filter_name_code.name_code)]
                self.write({'data': data, 'status': 200})


class QueryFutureHandler(BaseHandler):
    """模糊查询期货信息"""

    @try_except
    def post(self):
        query_str = self.get_argument('query_str', None)
        if query_str:
            df = pd.read_csv('future_list.csv')
            df_filter_symbol = df[df.order_book_id_symbol.str.contains(query_str)]
            if df_filter_symbol.empty:
                self.write({'data': '', 'status': 200})
            else:
                data = [{'code': k, 'name': v} for k, v in
                        zip(df_filter_symbol.order_book_id, df_filter_symbol.order_book_id_symbol)]
                self.write({'data': data, 'status': 200})


class StockKDataHandler(BaseHandler):
    """获取股票历史K线数据"""

    @try_except
    def post(self):
        asset_code = self.get_argument('asset_code', 'sh')  # 默认为上证指数
        ktype = self.get_argument('ktype', 'D')  # 默认为天级别数据
        start = self.get_argument('start', None)  # 开始时间
        end = self.get_argument('end', None)  # 结束时间
        k_his_data = ts.get_hist_data(code=asset_code, start=start, end=end, ktype=ktype)  # 调用tushare接口
        for ma in [5, 35]:
            k_his_data['MA_' + str(ma)] = pd.DataFrame.rolling(k_his_data['close'], ma).mean()
        if not k_his_data.empty:
            data = []  # echarts 需要的数据
            for i in k_his_data.index:
                data_one_day = []
                data_one_day.append(i)  # 时间0
                data_one_day.append(k_his_data['open'][i])  # 开盘价1
                data_one_day.append(k_his_data['close'][i])  # 收盘价2
                data_one_day.append(k_his_data['low'][i])  # 最低价3
                data_one_day.append(k_his_data['high'][i])  # 最高价4
                data_one_day.append(k_his_data['volume'][i])  # 成交量5
                data_one_day.append(0)  # tag6
                data_one_day.append(0)  # macd7
                data_one_day.append(0)  # dif8
                data_one_day.append(0)  # dea9
                if k_his_data['MA_5'][i] > k_his_data['MA_35'][i]:
                    data_one_day.append(1)  # 金叉10：短线上穿长线,展示全红
                    if data_one_day[1] > data_one_day[2]:  # 如果开盘价>收盘价,为了展示红,要将开盘价与收盘价位置互换一下
                        data_one_day[1], data_one_day[2] = data_one_day[2], data_one_day[1]
                elif k_his_data['MA_5'][i] <= k_his_data['MA_35'][i]:
                    data_one_day.append(0)
                    if data_one_day[1] < data_one_day[2]:  # 如果开盘价<收盘价,为了展示绿,要将开盘价与收盘价位置互换一下
                        data_one_day[1], data_one_day[2] = data_one_day[2], data_one_day[1]
                data.append(data_one_day)

            data.reverse()  # tushare 数据是从最近日期到过去，但是展示是从过去到最近
            self.write({'data': data, 'status': 200})
        else:
            self.write({'data': '', 'status': 200})


# class FutureKDataHandler(BaseHandler):
#     """获取期货历史K线数据"""
#
#     @try_except
#     def post(self):
#         asset_code = self.get_argument('asset_code', 'SC1906')
#         frequency = self.get_argument('ktype', 'D')
#         start_date = self.get_argument('start', None)
#         end_date = self.get_argument('end', None)
#         k_his_data = rq.get_price(asset_code, start_date=start_date, end_date=end_date, frequency=frequency)
#         for ma in [5, 35]:
#             k_his_data['MA_' + str(ma)] = pd.DataFrame.rolling(k_his_data['close'], ma).mean()
#         if not k_his_data.empty:
#             data = []  # echarts 需要的数据
#             for i in k_his_data.index:
#                 data_one_day = []
#                 data_one_day.append(i)  # 时间0
#                 data_one_day.append(k_his_data['open'][i])  # 开盘价1
#                 data_one_day.append(k_his_data['close'][i])  # 收盘价2
#                 data_one_day.append(k_his_data['low'][i])  # 最低价3
#                 data_one_day.append(k_his_data['high'][i])  # 最高价4
#                 data_one_day.append(k_his_data['volume'][i])  # 成交量5
#                 data_one_day.append(0)  # tag6
#                 data_one_day.append(0)  # macd7
#                 data_one_day.append(0)  # dif8
#                 data_one_day.append(0)  # dea9
#                 if k_his_data['MA_5'][i] > k_his_data['MA_35'][i]:
#                     data_one_day.append(1)  # 金叉10
#                     if data_one_day[1] > data_one_day[2]:  # 如果开盘价>收盘价,为了展示红,要将开盘价与收盘价位置互换一下
#                         data_one_day[1], data_one_day[2] = data_one_day[2], data_one_day[1]
#                 elif k_his_data['MA_5'][i] <= k_his_data['MA_35'][i]:
#                     data_one_day.append(0)  # 死叉10
#                     data_one_day[1], data_one_day[2] = data_one_day[2], data_one_day[1]
#                     if data_one_day[1] < data_one_day[2]:  # 如果开盘价<收盘价,为了展示绿,要将开盘价与收盘价位置互换一下
#                         data_one_day[1], data_one_day[2] = data_one_day[2], data_one_day[1]
#                 data.append(data_one_day)
#             data.reverse()  # 前端做了倒序，这里就不需要了
#             self.write({'data': data, 'status': 200})
#         else:
#             self.write({'data': '', 'status': 200})


application = tornado.web.Application([
    (r'/query_stock', QueryStockHandler),
    (r'/query_future', QueryFutureHandler),
    (r'/stock_k_data', StockKDataHandler),
    # (r'/future_k_data', FutureKDataHandler),
], )

if __name__ == '__main__':
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
