def print_timing(func):
    def wrapper(*args, **kwargs):
        t0 = time()
        res = func(*args, **kwargs)
        duration = (time() - t0)*1000.0
        print '%s took %0.3f ms' %(func.func_name, duration)
        return res
    return wrapper
