def square_root(x):
    if x < 0:
        return "undefined"
    if x == 0:
        return 0

    # Initial guess
    guess = x / 2.0
    
    # Loop until the guess is accurate enough
    while True:
        new_guess = (guess + x / guess) / 2
        if abs(new_guess - guess) < 1e-10:  # Convergence threshold
            return new_guess
        guess = new_guess
        
print (square_root(4))
