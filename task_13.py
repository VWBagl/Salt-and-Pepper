import time
from functools import wraps
from collections import OrderedDict

def cached(max_size=None, seconds=None):
    if max_size is not None:
        try:
            max_size = int(max_size)
            if max_size <= 0:
                max_size = None
        except (ValueError, TypeError):
            max_size = None
    
    if seconds is not None:
        try:
            seconds = float(seconds)
            if seconds <= 0:
                seconds = None
        except (ValueError, TypeError):
            seconds = None
    
    def decorator(func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]
                
                if seconds is None or current_time - timestamp <= seconds:
                    cache.move_to_end(key)
                    return result
                else:
                    del cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)
            
            return result
        return wrapper
    return decorator