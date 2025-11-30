def coincidence(spisok= [], range=None):

    if spisok == [] or range == None:
        return spisok
    
    result_list = []
    for i in spisok:
        if i in range:
            result_list.append(i)
    return result_list