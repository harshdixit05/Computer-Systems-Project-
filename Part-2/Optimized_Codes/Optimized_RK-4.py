def f(x):
    """Clean, focused function for original calculation"""
    import math
    return x * math.exp(x)

def first_derivative(x, h=0.0001):
    """Optimized first derivative calculation"""
    # Pre-calculate values to minimize repeated calculations
    x_minus_h = x - h
    h_half = h/2
    
    # Using built-in functions and minimizing operations
    k1 = f(x_minus_h)
    k2 = f(x_minus_h + h_half)
    k3 = f(x + h_half)
    k4 = f(x + h)
    
    return (k1 - 8*k2 + 8*k3 - k4)/(6*h)

def second_derivative(x, h=0.0001):
    """Optimized second derivative calculation"""
    # Pre-calculate to minimize operations
    k1 = f(x - h)
    k2 = f(x)
    k4 = f(x + h)
    
    return (k1 - 2*k2 + k4)/(h*h)

def main():
    # Pre-calculate range to minimize loop operations
    start = 1.5
    end = 2.5
    step = 0.1
    
    # Pre-allocate results list
    steps = int((end - start) / step) + 1
    results = []
    results.extend((0,0,0) for _ in range(steps))
    
    # Calculate results in batch for better cache usage
    for i, x in enumerate(range(int(start*10), int(end*10 + 1), int(step*10))):
        x = x/10
        fd = first_derivative(x)
        sd = second_derivative(x)
        results[i] = (x, fd, sd)
    
    # Output results
    print("\nResults:")
    print("{:<10} {:<15} {:<15}".format("x", "f'(x)", "f''(x)"))
    print("-" * 40)
    
    for x, fd, sd in results:
        print("{:<10.1f} {:<15.6f} {:<15.6f}".format(x, fd, sd))

if __name__ == "__main__":
    main()
