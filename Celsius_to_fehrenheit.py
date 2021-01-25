celsius = int(input())

def conv(c):
    return 9/5 * celsius + 32
    
fahrenheit = conv(celsius)
print(fahrenheit)