def secant_method(f, x0, x1, eps = 1e-7, max_counter = 1000, callback = None):
    counter = 0
    while abs(f(x1)) > eps and counter < max_counter:
        counter += 1
        x1, x0 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0)), x1
        if callback:
            err = abs(f(x1))
            callback(x0, x1, err, counter)
        
    if counter >= max_counter:
            raise Exception("exceed max_counter")
        
    return x1