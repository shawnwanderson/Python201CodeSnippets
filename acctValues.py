my_list = [(1, 5.54), (2, 10.45), (3, 2.50), (1, 63.32)]

reg_dict = {}

for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)
