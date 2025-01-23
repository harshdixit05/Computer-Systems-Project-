import numpy as np

def f(x):
    """Original function f(x) = x*exp(x)"""
    # Optimization: Use math.exp instead of np.exp for single values
    from math import exp
    return x * exp(x)

def calculate_derivatives(x, h=0.0001):
    """Calculate both derivatives at once to reduce function calls"""
    # Optimization: Calculate function values once and reuse
    fx = f(x)
    fx_plus_h = f(x + h)
    fx_minus_h = f(x - h)
    
    # Calculate both derivatives using stored values
    f_prime = (fx_plus_h - fx) / h
    f_double_prime = (fx_plus_h - 2*fx + fx_minus_h) / (h*h)
    
    return f_prime, f_double_prime

def main():
    """Main function to calculate and display derivatives"""
    # Optimization: Use direct iteration instead of creating array and list
    start, end, step = 1.5, 2.5, 0.1
    
    # Print header once
    print("\nNumerical Derivatives of f(x) = x*e^x using Euler's Method")
    print("-" * 50)
    print("{:^10} | {:^15} | {:^15}".format("x", "f'(x)", "f''(x)"))
    print("-" * 50)
    
    # Optimization: Direct iteration without storing results
    x = start
    while x <= end + step/2:  # Adding step/2 for floating point comparison
        f_prime, f_double_prime = calculate_derivatives(x)
        print("{:10.1f} | {:15.6f} | {:15.6f}".format(
            x, f_prime, f_double_prime))
        x += step

if __name__ == "__main__":
    main()