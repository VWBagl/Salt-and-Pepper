def sort_list(lst):
    if not lst:
        return []
    
    min_num = min(lst)
    max_num = max(lst)

    for i in range(len(lst)):
        if lst[i] == min_num:
            lst[i] = max_num
            
        elif lst[i] == max_num:
            lst[i] = min_num
            
    lst.append(min_num)
    return lst