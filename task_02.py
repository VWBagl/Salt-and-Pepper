def coincidence(spisok=None, rng=None):
    if spisok is None or rng is None:
        return []
    
    try:
        start = rng.start
        stop = rng.stop
    except AttributeError:
        return []
    
    result = []
    for i in spisok:
        try:
            if start <= i < stop:
                result.append(i)
        except (TypeError, ValueError):
            continue
    return result