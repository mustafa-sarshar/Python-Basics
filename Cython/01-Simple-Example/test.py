import timeit
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        times = int(sys.argv[2])
        py = timeit.timeit(stmt=f"code_py.factorial({num})", setup="import code_py", number=times)
        cy = timeit.timeit(stmt=f"code_cy.factorial({num})", setup="import code_cy", number=times)

        print(f"Num: {num}, times: {times}")
        print(f"In Python it took: {py:.8f}, but in Cython it took: {cy:.8f}")
        print(f"Python/Cython is {(py/cy):.2f}")
    else:
        print("No arguments are given. Please give the number and times the function should be executed.")

