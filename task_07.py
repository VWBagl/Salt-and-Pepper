def combine_anagrams(words_array):
    group = {}
    
    for i in words_array:
        letters_list = ''.join(sorted(i.lower()))
        
        if letters_list in group:
            group[letters_list].append(i)
        else:
            group[letters_list] = [i]
    
    return list(group.values())