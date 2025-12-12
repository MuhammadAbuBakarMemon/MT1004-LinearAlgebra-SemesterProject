
from utils import print_matrix

def solve_gauss_jordan(matrix, n_vars):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    print_matrix(matrix, "Initial Augmented Matrix")
    
    pivot_row = 0
    pivot_cols_indices = [] #

    for col in range(n_vars):
        if pivot_row >= rows:
            break


        max_row = pivot_row
        for r in range(pivot_row + 1, rows):
            if abs(matrix[r][col]) > abs(matrix[max_row][col]):
                max_row = r
        


        if abs(matrix[max_row][col]) < 1e-9:
            continue

        if max_row != pivot_row:
            matrix[pivot_row], matrix[max_row] = matrix[max_row], matrix[pivot_row]
            print_matrix(matrix, f"Swapped R{pivot_row+1} and R{max_row+1}")


        pivot_val = matrix[pivot_row][col]
        if abs(pivot_val - 1.0) > 1e-9:
            matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]
            print_matrix(matrix, f"R{pivot_row+1} / {pivot_val:.2f} (Normalize)")


        for r in range(rows):
            if r != pivot_row:
                factor = matrix[r][col]
                if abs(factor) > 1e-9:
                    new_row = []
                    for c_idx in range(cols):
                        val = matrix[r][c_idx] - factor * matrix[pivot_row][c_idx]
                        new_row.append(val)
                    matrix[r] = new_row
                    print_matrix(matrix, f"R{r+1} -> R{r+1} - ({factor:.2f} * R{pivot_row+1})")

        pivot_cols_indices.append(col)
        pivot_row += 1

    return matrix, pivot_cols_indices