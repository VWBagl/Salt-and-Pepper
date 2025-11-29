import re

def count_words(s):
    new_s = re.sub(r'[^a-zA-Z]', ' ', s.lower()).split()
    result_dict = {}

    for word in new_s:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
        
    return result_dict