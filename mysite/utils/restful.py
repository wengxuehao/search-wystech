from django.http import JsonResponse


class HttpCode(object):
    """
    定义状态码
    """
    ok = 200  # 正常请求
    params_error = 400  # 参数错误
    un_auth = 401  # 没有授权
    method_error = 405  # 请求方法错误
    server_error = 500  # 服务器内部错误


def result(code=HttpCode.ok, message='', count=None, data=None, kwargs=None):
    """
    定义函数　返回json数据
    :param code:
    :param message:
    :param count:
    :param data:
    :param kwargs:
    :return:
    """
    json_dict = {'code': code, 'count': count, 'message': message, 'data': data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        # 判断kwargs是否是字典以及是否有值
        json_dict.update(kwargs)

    return JsonResponse(json_dict)