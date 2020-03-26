def newton_method(f, f_foc,  initial, eps = 1e-10, max_counter = 1000):
    x = initial
    counter = 0
    
    while abs(f(x)) > eps and counter < max_counter:
        h = f(x)/f_foc(x)
        x = x - h
        counter += 1
    
    if counter >= max_counter:
        raise Exception("exceed max_counter")
    
    return x
    