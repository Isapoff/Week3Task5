# 1
# flag = True
# while flag:
#     num1,num2 = input('Enter your number:')
#     res = 0 
#     try:
#         res = int(num1) / int(num2)
#         print(res)
#         break
#     except ZeroDivisionError:
#         raise Exception('к сожалению на ноль делить нельзя') 
        

# 2
# flag = True
# while flag:
#     num1 = input()
#     num2 = input()
#     res = 0 
#     try:
#         res = int(num1) / int(num2)
#         print(res)
#         break
#     except ValueError:
#         raise Exception('Вы задали неправильный параметр, инпут ожидает число')
    
# 3
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     dict_['key3']
# except KeyError:
#     raise Exception('Нет такого ключа')



# 4
# wrd = input()


# try:
#    if wrd.startswith('[') and wrd.endswith(']'):
#        print(wrd)
#    elif wrd != wrd.startswith ('['):
#         raise Exception('Данная программа принимает только list')
# finally:
#     print()


# 5
# lists = [1, 2, 3, 4] 
# try:
#     lists[5]
# except IndexError:
#     print('4-последний индекс')










