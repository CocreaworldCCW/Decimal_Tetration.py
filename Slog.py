import math

def slog(a, x, tol=1e-6, max_iter=200):
    if x == a:
        return 1
    elif x == 1:
        return 0
    
    guess = 1
    for i in range(max_iter):
        tet_guess = tetration(a, guess)
        
        if abs(tet_guess - x) < tol:
            return guess
        
        guess -= (tet_guess - x) / (tet_guess * math.log(a) * guess)
        
    return None
