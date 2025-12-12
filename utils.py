import sys

def print_group_info():
    

    print("\n")
    print("LINEAR ALGEBRA PROJECT - GAUSS-JORDAN SOLVER")

    print("\n")
    print("Group Members:")
    print("1. Muhammad Abu Bakar (24K-0826)")
    print("2. Muhammad Furqan Sheikh(24K-0527)")
    print("\n")


def print_matrix(matrix, step_name=""):
    
    print(f"\n--- {step_name} ---")
    rows = len(matrix)
    for i in range(rows):
        # Format numbers to 2 decimal places for clarity
        row_str = "  ".join(f"{val:8.2f}" for val in matrix[i][:-1])
        constant = matrix[i][-1]
        print(f"[ {row_str} | {constant:8.2f} ]")
    print("-" * 40)

def get_input_matrix():
    
    print("=== Linear Equation Solver (Gauss-Jordan) ===")
    try:
        n_eq = int(input("Enter number of equations: "))
        n_vars = int(input("Enter number of variables: "))
    except ValueError:
        print("Error: Please enter integers.")
        sys.exit()

    matrix = []
    print(f"\nEnter the augmented matrix row by row.")
    print(f"Format: {n_vars} coefficients followed by the constant term.")
    print("Example (for 2x + 3y = 5): 2 3 5")

    for i in range(n_eq):
        while True:
            try:
                line = input(f"Equation {i+1}: ").strip()
                row = [float(x) for x in line.split()]
                
                if len(row) != n_vars + 1:
                    print(f"Error: Expected {n_vars + 1} numbers, got {len(row)}. Try again.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid number format. Use spaces between numbers.")
    
    return matrix, n_vars
