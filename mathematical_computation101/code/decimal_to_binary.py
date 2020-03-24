def decimal_to_binary(x):
    quotient, remainder = divmod(x, 2)
    res = str(remainder)
    while quotient > 0:
        quotient, remainder = divmod(quotient, 2)
        res = str(remainder) + res
    
    return res