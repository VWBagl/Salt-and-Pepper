def max_odd(array):
    num_list = []

    for i in array:
        if (type(i) is int or type(i) is float) and int(i) %2 !=0:
            num_list.append(int(i))
            
    if num_list:
        return max(num_list)
    else: return 