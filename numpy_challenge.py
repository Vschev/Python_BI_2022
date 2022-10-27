import numpy as np

if __name__ == "__main__":
    arr = np.eye(42)
    arrr = np.array(((10, 9, 22), (1, 4, 7)))
    arrrr = arrr[arrr < 18]
    arrrrrr = np.arange(1, 15, 7)
    fast = arrr.reshape(3, -1)


def matrix_multiplication(arg1, arg2):
    mult = np.matmul(arg1, arg2)
    return mult


def multiplication_check(your_list):
    result = True
    for elem in range(len(your_list) - 1):
        if your_list[elem].shape[1] == your_list[elem + 1].shape[0]:
            continue
        else:
            result = False
            break
    return result


def multiply_matrices(your_list):
    check = multiplication_check(your_list)
    if check:
        result = your_list[0]
        for elem in range(1, len(your_list)):
            result = np.matmul(result, your_list[elem])
    else:
        result = None
    return result


def compute_2d_distance(arg1, arg2):
    dist = np.linalg.norm(arg1 - arg2)
    return dist


def compute_multidimensional_distance(arg1, arg2):
    dist = np.linalg.norm(arg1 - arg2)
    return dist
