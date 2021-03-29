import re

def parse_str(data_str):
    res = []
    for x in re.split(",\s*", data_str):
        tmp = x.split()
        res.append(tmp if len(tmp) == 3 else tmp + [""])
    return res

def post_func(symbol_space, operation_list):
    i = 1
    worker_position = 0
    while(1):
        i -= 1
        current_operation = operation_list[1][i]
        if (current_operation == '!'):
            break
        if (current_operation == 'V'):
            symbol_space[worker_position] = '1'
            i = int(operation_list[2][i])
        if (current_operation == 'X'):
            symbol_space[worker_position] = '0'
            i = int(operation_list[2][i])
        if (current_operation == '<-'):
            if (worker_position==0):
                symbol_space = ['0'] + symbol_space
            else: worker_position -= 1
            i = int(operation_list[2][i])
        if (current_operation == '->'):
            if (worker_position==(len(symbol_space)-1)):
                symbol_space = symbol_space + ['0']
                worker_position += 1
            else: worker_position += 1
            i = int(operation_list[2][i])
        if (current_operation == '?'):
            if (symbol_space[worker_position]=='1'):
                string = operation_list[2][i]
                string = string.split(";")
                i = int(string[1])
            else:
                i = int(string[0])
    return symbol_space;



print("Enter symbol space:")
symbol_space = list(map(str, input().split()))
#print("Enter operation list:")
#operation_list = input()
operation_list = '1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5, 5 V 6, 6 !'       #Please, change operation list in this row
operation_list = list(map(list, zip(*parse_str(operation_list))))
#print(operation_list)
symbol_space = post_func(symbol_space, operation_list)
number = int(''.join(map(str, symbol_space)))  # -> 1234
print(number)


