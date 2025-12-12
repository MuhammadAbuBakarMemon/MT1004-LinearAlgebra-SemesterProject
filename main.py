
# all of these importing that i have done is from the files I have created above
from utils import print_group_info, get_input_matrix, print_matrix
from algorithm import solve_gauss_jordan
from analysis import classify_and_print_solution

if __name__ == "__main__":
    
    print_group_info()

    aug_matrix, num_vars = get_input_matrix()
    


    final_matrix, pivots = solve_gauss_jordan(aug_matrix, num_vars)
    
    print_matrix(final_matrix, "Final Reduced Matrix (RREF)")
    classify_and_print_solution(final_matrix, pivots, num_vars)