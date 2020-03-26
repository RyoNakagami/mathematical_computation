import numpy as np

def simp(f, a, b, N):
    '''
    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    
    dx = (b-a)/N
    x = np.linspace(a,b,N+1) # 区間をN個
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S