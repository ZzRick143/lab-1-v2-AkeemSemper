def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    total = (quarters *0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total
