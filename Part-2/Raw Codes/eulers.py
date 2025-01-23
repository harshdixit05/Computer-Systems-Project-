import numpy as np

def f(x):
    """Original function f(x) = x*exp(x)"""
    return x * np.exp(x)

def first_derivative(x, h=0.0001):
    """Calculate first derivative using forward difference"""
    return (f(x + h) - f(x)) / h

def second_derivative(x, h=0.0001):
    """Calculate second derivative using central difference"""
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

def calculate_derivatives(start, end, step):
    """Calculate derivatives for a range of x values"""
    x_values = np.arange(start, end + step, step)
    results = []
    
    for x in x_values:
        f_prime = first_derivative(x)
        f_double_prime = second_derivative(x)
        
        results.append({
            'x': x,
            'f_prime': f_prime,
            'f_double_prime': f_double_prime
        })
    
    return results

# Calculate derivatives for x = 1.5 to 2.5 with step 0.1
results = calculate_derivatives(1.5, 2.5, 0.1)

# Print results in a formatted table
print("\nNumerical Derivatives of f(x) = x*e^x using Euler's Method")
print("-" * 50)
print("{:^10} | {:^15} | {:^15}".format("x", "f'(x)", "f''(x)"))
print("-" * 50)

for result in results:
    print("{:10.1f} | {:15.6f} | {:15.6f}".format(
        result['x'],
        result['f_prime'],
        result['f_double_prime']))