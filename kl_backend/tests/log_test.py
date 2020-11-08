def try_except(func):
    """
    日志装饰器
    """

    def handle_problems(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            print({'error': '{}'.format(e),'status': 0})
            # logger.error(traceback.format_exc())

    return handle_problems

@try_except
def error_func(self):
    import requests
    return requests.get('www.google.com')


error_func('self')