def sort_list(list):
    min_num = min(list)
    max_num = max(list)

    for i in range(len(list)):
        if list[i] == min_num:
            list[i] = max_num

        elif list[i] == max_num:
            list[i] = min_num
            
    list.append(min_num)
    return list