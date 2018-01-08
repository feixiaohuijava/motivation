# # coding:utf-8
# def deco(*args,**kwargs):
#     print args
#     print kwargs
#     def _deco(func):
#         def __deco(*args, **kwargs):
#             print 'decorator args is', args
#             print 'before invoked'
#             ret = func(*args, **kwargs)
#             print 'after invoded'
#             print ret
#             return ret
#         return __deco
#     return _deco
#
# @deco('test',id="decorate")
# def f(a):
#     print 'f is invoked'
#     return a + 1
#
# f(6)