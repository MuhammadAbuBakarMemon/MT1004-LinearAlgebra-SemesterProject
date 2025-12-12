


def print_parametric_solution(matrix, pivot_cols, n_vars):
    """
    REQ: If infinite: solution in parameter form.
    """
    free_vars = []
    for j in range(n_vars):
        if j not in pivot_cols:
            free_vars.append(j)

    param_names = ['t', 's', 'r', 'u', 'v']
    
    print(f"Free Variables: {', '.join([f'x{j+1}' for j in free_vars])}")
    print("General Solution (Parametric Form):")
    
    for j in range(n_vars):
        if j in free_vars:
            
            p_idx = free_vars.index(j)
            p_name = param_names[p_idx % len(param_names)]
            print(f"x{j+1} = {p_name}")
        else:
            
            row_idx = -1
            for r in range(len(matrix)):
                if abs(matrix[r][j] - 1.0) < 1e-9:
                    row_idx = r
                    break
            
            if row_idx != -1:
                rhs = []
                constant = matrix[row_idx][-1]
                
                if abs(constant) > 1e-9:
                    rhs.append(f"{constant:.2f}")
                
                for fv in free_vars:
                    coeff = matrix[row_idx][fv]
                    if abs(coeff) > 1e-9:
                        p_idx = free_vars.index(fv)
                        p_name = param_names[p_idx % len(param_names)]
                        sign = "-" if coeff > 0 else "+"
                        val = abs(coeff)
                        rhs.append(f"{sign} {val:.2f}{p_name}")
                
                if not rhs:
                    print(f"x{j+1} = 0")
                else:
                    print(f"x{j+1} = {' '.join(rhs)}")

def classify_and_print_solution(matrix, pivot_cols, n_vars):
    """
    REQ: Correctly identify all three cases.
    REQ: If unique: numeric solution.
    REQ: If no solution: clear message.
    """
    rows = len(matrix)
    
    print("\n=== FINAL SOLUTION CLASSIFICATION ===")


    for r in range(rows):               # yeh no solution wala case check krti hai........
        all_zeros = all(abs(matrix[r][c]) < 1e-9 for c in range(n_vars))
        constant = matrix[r][-1]
        
        if all_zeros and abs(constant) > 1e-9:
            print("Status: No solution (inconsistent system)")
            print("Reason: Found a row corresponding to '0 = constant'.")
            return

    if len(pivot_cols) < n_vars:        # yeh infinite solutions li possibility 
        print("Status: Infinitely many solutions (dependent system)")
        print_parametric_solution(matrix, pivot_cols, n_vars)
        return

    print("Status: Unique solution")    #aur  yeh unique solutions ki.....
    for i, col_idx in enumerate(pivot_cols):
        for r in range(rows):
            if abs(matrix[r][col_idx] - 1.0) < 1e-9:
                val = matrix[r][-1]
                print(f"x{col_idx+1} = {val:.2f}")
                break