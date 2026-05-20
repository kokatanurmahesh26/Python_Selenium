# import logging
# logging.basicConfig(level=logging.DEBUG, 
#                     format='%(levelname)s:%(message)s')
# logger = logging.getlogger('Day-5')

# def safe_div(a,b) :
#     try :
#         return a/b
#     except ZeroDivisionError as e :
#         logger.error('Division by zero : %s, %s', a,b)
#         return None
#     except Exception as e :
#         logger.exception('Unexcepted error')
#         return None  
# print('10/2 = ', safe_div(10,2))
# print('10/0 = ', safe_div(10,0))
