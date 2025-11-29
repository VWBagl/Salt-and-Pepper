def connect_dicts(dict1, dict2):
    sum_1 = sum(dict1.values())
    sum_2 = sum(dict2.values())
    
    if sum_1 > sum_2:
        first_dict, second_dict = dict1, dict2
    else:
        first_dict, second_dict = dict2, dict1
    
    result = {}
    for key, value in first_dict.items():
        if value >= 10:
            result[key] = value
    
    for key, value in second_dict.items():
        if value >= 10 and key not in result:
            result[key] = value
    
    return dict(sorted(result.items(), key=lambda item: item[1]))