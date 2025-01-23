def f(x):
    """Original function f(x) = x*exp(x)"""
    import math
    return x * math.exp(x)

def first_derivative(x, h=0.0001):
    """Calculate first derivative using RK4 method"""
    k1 = f(x - h)
    k2 = f(x - h/2)
    k3 = f(x + h/2)
    k4 = f(x + h)
    
    return (k1 - 8*k2 + 8*k3 - k4)/(6*h)

def second_derivative(x, h=0.0001):
    """Calculate second derivative using RK4 method"""
    k1 = f(x - h)
    k2 = f(x)
    k4 = f(x + h)
    
    return (k1 - 2*k2 + k4)/(h*h)

def main():
    start = 1.5
    end = 2.6
    step = 0.1
    
    print("\nResults:")
    print("{:<10} {:<15} {:<15}".format("x", "f'(x)", "f''(x)"))
    print("-" * 40)
    
    x = start
    while x <= end:
        fd = first_derivative(x)
        sd = second_derivative(x)
        print("{:<10.1f} {:<15.6f} {:<15.6f}".format(x, fd, sd))
        x += step

if __name__ == "__main__":
    main()
