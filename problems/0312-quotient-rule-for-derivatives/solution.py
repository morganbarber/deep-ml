import numpy as np

def evaluate(coeffs, x):
    p, dp = 0.0, 0.0
    for c in coeffs:
        dp = dp * x + p
        p = p * x + c
    return p, dp

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g, dg = evaluate(g_coeffs, x)
    h, dh = evaluate(h_coeffs, x)
    
    if h == 0:
        raise ValueError("denominator cannot be 0")
    
    return ((dg * h) - (g * dh)) / (h ** 2) 