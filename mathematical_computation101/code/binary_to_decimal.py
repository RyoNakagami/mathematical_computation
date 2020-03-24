def binary_to_decimal_1(x):
    import re
    
    if not isinstance(x, str):
        raise ValueError('引数が文字列ではありません')
    condition_1 = re.findall('\D|[2-9]', x)
    
    if condition_1:
        print(condition_1)
        raise ValueError('引数に不正な文字列が入っています')
    
    res = 0
    length = len(x) - 1
    for i, j in enumerate(x):
        i = length - i
        res += int(j) * (2 ** (i))
        
    return res

def binary_to_decimal_2(x):
    import re
    if not isinstance(x, str):
        raise ValueError('引数が文字列ではありません')
    condition_1 = re.findall('\D|[2-9]', x)
    
    if condition_1:
        print(condition_1)
        raise ValueError('引数に不正な文字列が入っています')
    
    x = int(x)
    base = 0
    res = 0
    while x:
        digit = x % 10
        res += (2 ** base) * digit
        
        base += 1
        x = int(x / 10)
        
    return res

if __name__ == "__main__":
    print(binary_to_decimal_2('00101001'))