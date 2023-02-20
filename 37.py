'''Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
chickens do we have?
'''

def solve_puzzle(heads, legs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if 2 * chickens + 4 * rabbits == legs:
            return rabbits, chickens
    return None

rabbits, chickens = solve_puzzle(35, 94)
if rabbits is not None:
    print("Number of rabbits:", rabbits)
    print("Number of chickens:", chickens)
else:
    print("No solution found")
