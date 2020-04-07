# Bisection method
## Global

a = 2.0
LIMIT = 1e-10 ## because we use float 64 (m: 52 bit)

## define finction
def f(x):
    return x * x - a

## set initial value
def bisection_method():

    x_upper = float(input('input upper initial value '))
    x_lower = float(input('input lower initial value '))
    counter = 0

    if f(x_upper) * f(x_lower) > 0:
        raise InputError('wrong initial input value, f(x) are not opposite-signed')
    
    while (abs(x_upper - x_lower) > LIMIT) & (counter < 100):
        x_mid = (x_upper + x_lower) / 2
        if f(x_mid) > 0:
            x_upper = x_mid
        else:
            x_lower = x_mid
        print("{:.15f} {:.15f}".format(x_lower, x_upper))
        counter += 1
    
    return x_lower, x_upper
    
if __name__ == "__main__":
    bisection_method()
    

    

